# 🤖 AI Chatbot with Gemini & Streamlit

A simple AI chatbot web application built using **Streamlit** and **Google Gemini API**. This project allows users to interact with Google's Gemini model through a clean and interactive chat interface.

---

## 🚀 Features

* Interactive chatbot UI using Streamlit
* Integration with Google Gemini API
* Chat history using Streamlit session state
* Simple and beginner-friendly project structure
* Environment variable support using `.env`

---

## 📂 Project Structure

```bash
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Generative AI (Gemini API)
* python-dotenv

---

## 📋 Requirements

* Python 3.10+
* Gemini API Key

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Never upload your real API key to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will start locally and can be accessed in your browser.

---

## 💬 Example Usage

1. Open the Streamlit app.
2. Type your message in the chat input.
3. Receive AI-generated responses from Gemini.

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

## 🔒 Security Note

Do not expose your `.env` file or API keys publicly.
Add `.env` to your `.gitignore` file:

```gitignore
.env
```

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you like this project, consider giving it a star on GitHub.


