import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def scrape_text(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join(p.get_text() for p in paragraphs)[:4000]
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return ""

def summarize_with_groq(text, topic):
    endpoint = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
    "Authorization": f"Bearer {st.secrets.get('GROQ_API_KEY') or os.getenv('GROQ_API_KEY')}",
    "Content-Type": "application/json"
    }
    body = {
        "model": "llama3-70b-8192",
        "temperature": 0.8,
        "max_tokens": 8192,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a highly knowledgeable research assistant. "
                    "Generate a comprehensive and in-depth summary of the content provided. "
                    "Ensure you cover all key arguments, supporting evidence, real-world applications, and implications. "
                    "Include relevant subheadings if needed."
                )
            },
            {
                "role": "user",
                "content": f"Research topic: {topic}\n\n{text}"
            }
        ]
    }

    try:
        response = requests.post(endpoint, headers=headers, json=body)
        res_json = response.json()

        if "choices" in res_json:
            return res_json["choices"][0]["message"]["content"]
        elif "error" in res_json:
            return f"❌ Groq API error: {res_json['error'].get('message', 'Unknown error')}"
        else:
            return "❌ Unexpected response from Groq."
    except Exception as e:
        return f"❌ Request failed: {e}"

def interactive_qna(summary_text, topic):
    endpoint = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    print("\nYou can now ask follow-up questions about the summary. Type 'exit' to quit.\n")

    while True:
        user_question = input("❓ Your question: ").strip()
        if user_question.lower() == "exit":
            print("Goodbye!")
            break

        prompt = (
            f"You are a helpful research assistant. Use the following summary context to answer the question.\n\n"
            f"Summary:\n{summary_text}\n\n"
            f"Question about '{topic}': {user_question}"
        )

        body = {
            "model": "llama3-70b-8192",
            "temperature": 0.7,
            "max_tokens": 1000,
            "messages": [
                {"role": "system", "content": "You are a helpful research assistant."},
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post(endpoint, headers=headers, json=body)
            res_json = response.json()

            if "choices" in res_json:
                answer = res_json["choices"][0]["message"]["content"]
                print(f"\n🤖 Answer:\n{answer}\n")
            else:
                print("❌ Unexpected API response.")
        except Exception as e:
            print(f"❌ Request failed: {e}")