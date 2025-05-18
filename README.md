# 🍽️ Barbeque Nation Chatbot (Voice & Chat-based Booking System)

This project is a full-stack AI assistant for **Barbeque Nation**, designed to handle:

- Customer FAQs
- Table bookings
- Booking modifications/cancellations
- Conversation logging to Google Sheets
- Voice/chat interface with state-machine-based prompt handling

Built using:
- 🧠 Retell AI & AgentOps Framework (for voice/chat)
- ⚙️ FastAPI backend (Python)
- 💬 React + Vite frontend (Chat UI)
- 📄 Google Sheets API (logging conversations)

---

## 🚀 Features

- ✅ State-machine-based flow control using Jinja2 templated prompts
- ✅ FastAPI endpoints for handling agent requests, knowledge base, and logging
- ✅ Google Sheets logging for incoming conversations
- ✅ Retell AI-compatible backend APIs
- ✅ Clean React UI for chatbot interaction
- ✅ TailwindCSS + Vite for rapid frontend dev

---


---

## 🛠️ Setup Instructions

### 1. Backend (FastAPI)

```bash
# Create virtual environment and activate
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt

# Run FastAPI app
uvicorn backend.main:app --reload
---

## 2. Frontend (React)
cd frontend
npm install
npm run dev

---

🔐 Google Credentials
🔒 Your google_credentials.json is excluded from version control (.gitignore)

To enable Google Sheets logging:

Go to Google Cloud Console.

Create a service account and enable Google Sheets API.

Download google_credentials.json and place it in data/.

Share the target Google Sheet with the service account email.

---

📡 API Endpoints
POST /agent — Main Retell AI webhook

GET /knowledge_base — Serve KB entries

POST /log — Log conversation to Google Sheets

---

🙋‍♀️ Author
C Sai laxmi Gayatri
GitHub: @CSGayatri


