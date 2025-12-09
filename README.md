# Gupp Shupp Sathi (Companion AI)

**Gupp Shupp Sathi** is an intelligent, multilingual AI companion designed to understand you better over time. It doesn't just chat; it *remembers* your preferences, emotional patterns, and facts to provide personalized, empathetic, and culturally relevant responses in **English and Hindi (Hinglish)**.

## 🌟 Key Features

### 🧠 1. Long-Term Memory (Memex)
Unlike standard chatbots that forget you after a session, Gupp Shupp Sathi remembers. It uses a sophisticated extraction engine to analyze your conversations and build a persistent profile:
*   **Facts:** Remembers personal details (e.g., "I'm a night owl", "I live in Udaipur").
*   **Preferences:** Tracks what you like and dislike (e.g., "Hates early mornings", "Loves dark mode").
*   **Emotional Patterns:** Identifies your emotional triggers (e.g., "Anxiety on Friday evenings").
*   **Anti-Hallucination:** Strictly constrained to only remember what you explicitly say, ensuring accuracy.

### 🎭 2. Dynamic Personalities
The AI adapts its tone and style to match your emotional needs. You can switch instantly between:
*   **Calm Elder-Brother Mentor:** Provides composed, mature, and practical advice. Speaks in respectful Hinglish and focuses on actionable steps without lecturing.
*   **Witty Desi Dost:** Your fun, casual friend. Uses emojis, light teasing, and informal Hinglish (like "Arre yaar, relax..."). Perfect for lightening the mood.
*   **Warm Reflective Therapist:** A supportive listener who validates your feelings. Uses gentle, open-ended questions and offers insights based on your history, strictly avoiding unsolicited advice.

### 🌏 3. Seamless Multilingual Support (Hinglish)
Communicate naturally in the language you're most comfortable with.
*   **Context-Aware:** The AI understands English, Hindi, and the mix of both (Hinglish).
*   **Adaptive Response:** It replies in the same language/style you use, making the conversation feel authentic and culturally grounded.

### ⚡ 4. Context-Aware Rewriting Engine
This is the core intelligence of the system.
1.  **Ingest:** It takes a standard AI response.
2.  **Contextualize:** It retrieves relevant memories (facts/patterns) from the Memex.
3.  **Rewrite:** It completely rewrites the response to match the selected personality *and* explicitly references your memories (e.g., "Since you're a night owl [Fact], maybe try...").
4.  **Result:** A response that feels like it comes from someone who truly knows you.
## 🛠️ Tech Stack

*   **LLM:** Groq API (`openai/gpt-oss-120b`) for high-speed, reasoning-capable inference.
*   **Backend:** FastAPI for the REST API (`/ingest`, `/rewrite`).
*   **Frontend:** Streamlit for an interactive chat interface.
*   **Memory:** Custom Pydantic models for structured data extraction.

## 🚀 Getting Started

### Prerequisites
*   Python 3.8+
*   A Groq API Key

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AnkithGoje/gupp-shupp-sathi.git
    cd gupp-shupp-sathi
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # Mac/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root directory and add your Groq API key:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

### Running the Application

You need to run both the backend and frontend terminals.

**1. Start the Backend API:**
```bash
uvicorn api.main:app --reload
```
*Server runs at `http://127.0.0.1:8000`*

**2. Start the Frontend UI:**
```bash
streamlit run demo/streamlit_app.py
```
*App opens in your browser at `http://localhost:8501`*
## 📂 Project Structure
```
companion/
├── api/
│   └── main.py              # **FastAPI Backend**: Defines the `/ingest` (memory) and `/rewrite` (personality) endpoints.
│
├── demo/
│   └── streamlit_app.py     # **Frontend UI**: The interactive chat interface built with Streamlit. Handles user input and displays responses.
│
├── memex/                   # **Memory Module**: The "Brain" of the AI.
│   ├── extractor.py         # Logic to extract facts, preferences, and patterns from chat history using the LLM.
│   ├── models.py            # Pydantic models defining the structure of extracted memory (Fact, Preference, EmotionalPattern).
│   └── prompts.py           # The system prompts used to guide the LLM in extracting structured data without hallucinations.
│
├── personality/             # **Personality Module**: The "Voice" of the AI.
│   ├── engine.py            # The core logic that rewrites raw answers into the selected persona, injecting memory context.
│   └── tones.yaml           # Configuration file defining the system prompts, temperature, and max_tokens for each personality (Mentor, Dost, Therapist).
│
├── requirements.txt         # List of all Python libraries required to run the project.
├── .env                     # Configuration file for storing secrets like `GROQ_API_KEY` (Excluded from Git).
└── .gitignore               # Specifies which files and directories Git should ignore.
```

## 🌟 Star Us

If you find this project useful, please ⭐ the repository. It helps support the project!
