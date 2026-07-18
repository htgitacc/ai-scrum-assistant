# 🤖 AI Scrum Assistant (A/B Model Testing Tool)

> An AI-powered tool that transforms raw, unstructured ideas into structured Agile documentation, with a focus on security and operational risks. Built to demonstrate AI workflow orchestration and model evaluation skills.

[🇭🇺 Magyar leírás lentebb](#magyar-leírás)

---

## 🎯 What is this?

This is a **Streamlit-based web application** that acts as an "AI team member" for Scrum Masters, Product Owners, and IT teams. It takes raw meeting notes or rough ideas and generates:

1. 📝 **User Stories** (in standard format)
2. ✅ **Acceptance Criteria** (Given/When/Then)
3. ⚠️ **Security & Operational Risks** (with mitigations)

### What makes it unique?
- **🌐 Bilingual support**: Switch between English and Hungarian on the fly
- **🧠 A/B Model Testing**: Compare different LLMs (e.g., Llama 3.1 8B vs 70B) side-by-side
- **🔒 Security-first mindset**: Built-in risk analysis leveraging IT security expertise
- **🆓 Open-source API**: Uses [clod.io](https://clod.io) free tier with OpenAI-compatible endpoints

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | [Streamlit](https://streamlit.io/) |
| AI Backend | OpenAI-compatible API via [clod.io](https://clod.io) |
| Models | Llama 3.1 (8B/70B), Qwen 2.5, and more |
| Config | Python `dotenv` for secure environment variables |

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/htgitacc/ai-scrum-assistant.git
cd ai-scrum-assistant
```

### 2. Create a virtual environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install streamlit openai python-dotenv
```

### 4. Configure environment variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_clod_io_api_key_here
OPENAI_BASE_URL=https://api.clod.io/v1
AI_MODEL=llama-3.1-8b
```

> 🔑 Get a free API key at [clod.io](https://clod.io) (100 free requests/day, 50+ models)

### 5. Run the app
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

**If the following text pops up, feel free to close it, it is not needed to run the program. During installation, 2 hidden libraries are created, which can be useful when further developing the code with AI agents. It can be installed at any time.**
"Help agents write better apps. Install the official Streamlit skills so AI coding agents can build and debug your apps."

---

## 📸 Screenshots

<!-- Add screenshots here later -->
<!-- ![English mode](screenshots/english.png) -->
<!-- ![Hungarian mode](screenshots/hungarian.png) -->

---

## 🎓 Learning Outcomes

This project was built as part of a personal upskilling journey. Key takeaways:

- **Model evaluation**: Discovered that smaller models (8B) struggle with structured Hungarian output, while larger ones (70B+) perform well. Built the A/B tester to validate this empirically.
- **API abstraction**: Leveraged OpenAI-compatible endpoints to access 50+ open-source models without vendor lock-in.
- **Security by design**: Integrated risk analysis directly into the Agile workflow — a pattern I've seen missing in most AI tools.
- **Prompt engineering**: Crafted domain-specific system prompts that combine Scrum Master and IT Security expertise.

---

## 🗺️ Roadmap

- [ ] Export results to Markdown/PDF
- [ ] Integration with Jira / Azure DevOps via n8n
- [ ] Conversation history with session state
- [ ] Custom prompt templates per role (PO, SM, Dev)

---

## 📬 Contact

Built by **xyo** — IT Security Specialist turned AI-Augmented Agile Practitioner.

[LinkedIn](https://www.linkedin.com/in/tiborhanak/) | [GitHub](https://github.com/htgitacc/)

---

## 📄 License

MIT License — feel free to use, modify, and share.

---
---

# 🇭🇺 Magyar leírás

## 🎯 Mi ez?

Egy **Streamlit alapú webalkalmazás**, ami "AI csapattagként" működik Scrum Masterek, Product Ownerek és IT csapatok számára. Nyers meeting jegyzetekből vagy vázlatos ötletekből generál:

1. 📝 **User Story-kat** (szabványos formátumban)
2. ✅ **Acceptance Critériumokat** (Given/When/Then)
3. ⚠️ **Biztonsági és Üzemeltetési Kockázatokat** (mitigációkkal)

### Mi teszi egyedivé?
- **🌐 Kétnyelvű támogatás**: Angol és magyar nyelv közötti dinamikus váltás
- **🧠 A/B Modell Teszt**: Különböző LLM-ek összehasonlítása (pl. Llama 3.1 8B vs 70B)
- **🔒 Biztonság-fókusz**: Beépített kockázatelemzés IT biztonsági szakértelemmel
- **🆓 Nyílt forráskódú API**: [clod.io](https://clod.io) ingyenes szintjének használata OpenAI-kompatibilis végpontokkal

## 🎓 Tanulási pontok

- **Modell értékelés**: Felismertem, hogy a kisebb modellek (8B) nehezen kezelik a strukturált magyar kimenetet, míg a nagyobbak (70B+) jól teljesítenek. Ezt empirikusan validáltam az A/B teszterrel.
- **API absztrakció**: OpenAI-kompatibilis végpontokat használtam, így 50+ nyílt forráskódú modell érhető el szolgáltatói lock-in nélkül.
- **Biztonság tervezési szinten**: A kockázatelemzést közvetlenül az agilis workflow-ba integráltam — ez a minta a legtöbb AI eszközből hiányzik.
- **Prompt mérnökség**: Domain-specifikus system promptokat készítettem, amelyek ötvözik a Scrum Master és IT biztonsági szakértelmet.

## 📬 Kapcsolat

Készítette: **xyo** — IT biztonsági szakértőből AI-megerősített agilis szakember.

[LinkedIn](https://www.linkedin.com/in/tiborhanak/) | [GitHub](https://github.com/htgitacc)
