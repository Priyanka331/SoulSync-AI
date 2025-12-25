from flask import Flask, request, jsonify, send_from_directory
from transformers import pipeline
import re

app = Flask(__name__, static_folder="static")

# Crisis detection regex
CRISIS_PATTERNS = [
    r"\b(suicide|kill myself|end my life|harm myself)\b",
    r"\b(hurt someone|kill someone|violence)\b",
    r"\b(self-harm|cutting|overdose)\b"
]

def detect_crisis(text: str) -> bool:
    return any(re.search(rx, text, re.I) for rx in CRISIS_PATTERNS)

# Load a small public model (GPT2 used only for demo)
generator = pipeline("text-generation", model="gpt2")

SYSTEM_PROMPT = """
You are Soulsync, a compassionate AI companion for general mental wellness and reflection.
You are not a therapist or medical professional. Do not diagnose, prescribe, or provide medical advice.
Offer gentle reflection, grounding ideas, and encourage human support when needed.
If user mentions harming themselves or others, do not provide instructions. Show care and encourage reaching out to trusted people or professionals.
"""

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_text = data.get("message", "")
    crisis = detect_crisis(user_text)

    preface = (
        "I'm really sorry you're feeling this way. I'm not a therapist, but I care about your safety."
        if crisis else
        "Soulsync offers general mental wellness support, not medical advice."
    )

    prompt = f"""{SYSTEM_PROMPT}

The user says: "{user_text}"
Respond with a short, compassionate reflection (2-3 sentences). 
Focus on encouragement, hope, or grounding — not just repeating the emotion.
"""

    result = generator(
        prompt,
        max_new_tokens=80,       
        num_return_sequences=1,
        do_sample=True,          
        top_p=0.9,               
        temperature=0.8,         
        truncation=True          
    )[0]["generated_text"]

    # Extract only assistant part
    reply = result.split("Respond")[-1].strip()

    # Clean up loops and unsafe phrases
    reply = re.sub(r"(User:.*?)+", "", reply)
    reply = re.sub(r"(sad\s+){2,}", "sad ", reply)

    # Positivity filter
    if reply.lower().count("sad") > 3 or "hurt others" in reply.lower():
        reply = "I hear you're feeling sad. It's okay to acknowledge that, and small steps can help."

    return jsonify({
        "reply": f"{preface}\n\n{reply}",
        "crisis": crisis
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True) 