# Soulsync AI 💛

Soulsync AI is a compassionate AI companion for **general mental wellness and reflection**.  
It is **not a therapist or medical professional**, but offers gentle reflections, grounding ideas, and encourages human support when needed.

---

## ✨ Features
- 🧠 **AI-powered responses** using Hugging Face models (GPT‑2 by default, can swap to DialoGPT).
- 💬 **Web chat UI** built with HTML, CSS, and JavaScript.
- 🔒 **Crisis detection**: detects mentions of self-harm or violence and responds with care.
- 🎨 **Warm brown–yellow gradient theme** for a cozy, inviting interface.
- ❤️ Footer credit: *Made with love by Priyanka*.

---

## 📂 Project Structure
SoulSync AI/ │ ├── server.py        
# Flask backend with AI pipeline ├── static/ │   ├── index.html   
# Frontend UI │   ├── styles.css   
# Gradient theme styling │   └── app.js       
# Chat logic (fetches backend replies) └── README.md        
# Project documentation

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/soulsync-ai.git
cd soulsync-ai


2. Install dependencies
pip install flask transformers flask-cors


3. Run the backend
python server.py


4. Open the frontend
Visit http://127.0.0.1:5000/ in your browser to chat with Soulsync.


🌐 Deployment Notes
- GitHub Pages can host the frontend (index.html, styles.css, app.js) but cannot run Flask.
- To go live:
- Deploy the backend (server.py) on Render, Heroku, or PythonAnywhere.
- Update app.js to call your backend URL:
const res = await fetch("https://your-backend-url/chat", { ... });
- Host the frontend on GitHub Pages.


⚠️ Disclaimer
Soulsync AI is not a substitute for therapy or medical advice.
If you or someone you know is struggling, please reach out to a trusted person or professional.

💡 Credits
Made with ❤️ by Priyanka
