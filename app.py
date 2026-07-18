import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Környezeti változók betöltése a .env fájlból
load_dotenv()

# OpenAI kliens inicializálása a clod.io végponttal
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.clod.io/v1")
)

# Oldal beállítása
st.set_page_config(page_title="AI Scrum Assistant", page_icon="🤖", layout="centered")

# --- 1. BEÁLLÍTÁSOK (Sidebar vagy felső sáv) ---
col1, col2 = st.columns(2)

with col1:
    lang = st.selectbox(
        "🌐 Nyelv / Language", 
        ["English", "Magyar"]
    )

with col2:
    # FONTOS: Cseréld le ezeket a modellekre a clod.io dashboardon pontosan látható nevekre!
    model_options = [
        os.getenv("AI_MODEL", "llama-3.1-8b"),
        "Gemma 4 31B IT",
        "Qwen 3.5 9B"
    ]
    model_options = list(dict.fromkeys(model_options))
    
    selected_model = st.selectbox(
        "🧠 AI Modell", 
        model_options
    )

# --- 2. NYELVFÜGGŐ SZÖVEGEK ÉS PROMPTOK ---
if lang == "English":
    st.title("🤖 AI Scrum Assistant (A/B Model Test)")
    st.markdown("""
    This tool transforms raw, unstructured ideas into structured Agile documentation. 
    With the built-in **language** and **model selector**, you can instantly compare the performance of different AI models in both English and Hungarian.
    """)
    placeholder_text = "E.g., I want users to be able to upload a PDF, and the system should extract the date from it, but they should only see their own documents..."
    btn_text = "🚀 Generate Documentation"
    system_prompt = """You are an expert Scrum Master and IT Security Specialist. Your task is to transform the user's raw, unstructured idea or meeting notes into structured Agile documentation. 
Output STRICTLY in well-formatted Markdown with the following sections:
1. 📝 **User Story** (As a [role], I want to [action], so that [benefit])
2. ✅ **Acceptance Criteria** (Given/When/Then format, 3-5 points)
3. ⚠️ **Security & Ops Risks** (Potential data privacy, access control, or operational risks, along with suggested mitigations)."""
    loading_text = "AI is working on it..."
    success_text = "Success!"
    error_text = "API Error"
    tip_text = "💡 **Tip:** Check your `.env` file (API key, Base URL, and ensure the selected model name exactly matches clod.io's available models)."

else: # Magyar
    st.title("🤖 AI Scrum Asszisztens (A/B Modell Teszt)")
    st.markdown("""
    Ez az eszköz nyers, rendezetlen ötletekből generál strukturált agilis dokumentációt. 
    A beépített **nyelv-** és **modellválasztóval** azonnal összehasonlíthatod a különböző AI modellek teljesítményét magyar és angol nyelven.
    """)
    placeholder_text = "Pl.: Azt akarom, hogy a felhasználó tudjon feltölteni PDF-et, és a rendszer olvassa ki belőle a dátumot, de csak a saját dokumentumait lássa..."
    btn_text = "🚀 Dokumentáció Generálása"
    system_prompt = """Te egy tapasztalt Scrum Master és IT biztonsági szakértő vagy. Feladatod, hogy a felhasználó nyers, rendezetlen ötletéből strukturált agilis dokumentációt készíts. 
A válaszod kizárólag jól olvasható Markdown formátum legyen, a következő szekciókkal:
1. 📝 **User Story** (Mint [szerepkör], szeretném [cselekvés], hogy [előny])
2. ✅ **Acceptance Criteria** (Given/When/Then formátumban, 3-5 pont)
3. ⚠️ **Security & Ops Risks** (Potenciális adatvédelmi, hozzáférési vagy üzemeltetési kockázatok, és javasolt mitigáció)."""
    loading_text = "Az AI csapattag éppen dolgozik..."
    success_text = "Sikeres generálás!"
    error_text = "Hiba történt"
    tip_text = "💡 **Tipp:** Ellenőrizd a `.env` fájlt, és győződj meg róla, hogy a kiválasztott modell neve pontosan egyezik a clod.io által kínáltakkal."

# --- 3. ALKALMAZÁS LOGIKA ---
raw_idea = st.text_area("Input / Bemenet:", placeholder=placeholder_text, height=150)

if st.button(btn_text):
    if not raw_idea.strip():
        st.warning("Please enter an idea first! / Kérlek, írj be egy ötletet a fenti mezőbe!")
    else:
        with st.spinner(loading_text):
            try:
                response = client.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": raw_idea}
                    ],
                    temperature=0.7
                )
                
                st.success(success_text)
                
                # Modell neve kiírása az eredmény fölé
                if lang == "English":
                    st.info(f"🤖 Result from model: **{selected_model}**")
                else:
                    st.info(f"🤖 Eredmény a következő modellel: **{selected_model}**")
                
                st.markdown(response.choices[0].message.content)
                
                # Másolható kód blokk
                st.code(response.choices[0].message.content, language="markdown")

            except Exception as e:
                st.error(f"{error_text}: {e}")
                st.info(tip_text)