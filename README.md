# 🤖 AI Chatbot with Gemini & Streamlit

A simple and interactive AI chatbot web application built using **Streamlit** and **Google Gemini API**.  
This project allows users to chat with Google's Gemini model through a clean web interface.

---

## 🚀 Features

- 💬 Interactive chatbot UI using Streamlit
- 🤖 Integration with Google Gemini API
- 📝 Chat history using Streamlit Session State
- 🔐 Secure API key management with `.env`
- 🧩 Beginner-friendly project structure

---

## 📂 Project Structure

```bash
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Generative AI (Gemini API)
- python-dotenv

---

## 📋 Requirements

Before running the project, make sure you have:

- Python 3.10 or higher
- A Google Gemini API Key

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables

Create a `.env` file in the project root directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

⚠️ **Important:** Never upload your real API key to GitHub.

---

## 🔒 Create a `.gitignore` File

To keep sensitive files safe, create a `.gitignore` file and add:

```gitignore
# Virtual Environment
venv/

# Environment Variables
.env

# Python Cache
__pycache__/
*.pyc

# Streamlit
.streamlit/

# VS Code
.vscode/
```

This prevents your API keys and unnecessary files from being uploaded to GitHub.

---

## ▶️ Run the Application

Start the Streamlit app using:

```bash
streamlit run app.py
```

The application will open in your browser automatically.

---

## 💬 Example Usage

1. Open the Streamlit app
2. Type your message in the chat input
3. Receive AI-generated responses from Gemini

---

## 📸 Preview

A simple chatbot interface powered by Gemini AI.

---

## 📌 Dependencies

```txt
streamlit
google-generativeai
python-dotenv
```

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!


