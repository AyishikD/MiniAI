# 🧠 AI Mini Knowledge

AI Mini Knowledge is a smart research assistant built with **Streamlit** that searches the web for any topic, summarizes the findings using **Groq's LLaMA 3** models, and lets users ask intelligent follow-up questions — all within a beautiful and interactive interface.

## 🚀 Features

- 🔍 Web search using [ScraperAPI](https://www.scraperapi.com/)
- 📄 Summarizes top search results using Groq's `llama3-70b-8192`
- 🤖 Asks and answers follow-up questions contextually
- 💬 Session memory for Q&A and summaries
- 🔑 User-friendly interface to input API keys (no .env required)

---

## 🧰 Tech Stack

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Groq API](https://console.groq.com/)
- [ScraperAPI](https://www.scraperapi.com/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

---

## 📦 Installation

```bash
git clone https://github.com/AyishikD/MiniAI
cd MiniAI
pip install -r requirements.txt
````

---

## 🔐 Required API Keys

* **Groq API Key:** [Get it here](https://console.groq.com/)
* **ScraperAPI Key:** [Get it here](https://www.scraperapi.com/)

> No need to use a `.env` file — you can enter keys directly in the app.

---

## 🖥️ Run the App

```bash
streamlit run app.py
```

---

## ✨ How It Works

1. **Enter a topic** — e.g., *impact of AI on healthcare*
2. **App fetches** top web pages using ScraperAPI
3. **Scrapes and summarizes** the results using LLaMA 3
4. **Allows follow-up Q\&A** powered by Groq with session memory

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📝 License

MIT License. See [LICENSE](LICENSE) for more info.

---
