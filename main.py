from scraper import get_search_links
from summarizer import scrape_text, summarize_with_groq, interactive_qna  

def main():
    topic = input("🔍 Enter your research topic: ")
    links = get_search_links(topic)

    if not links:
        print("No links found.")
        return

    print(f"\n🌐 Found {len(links)} results. Summarizing...\n")
    combined_text = ""
    for link in links:
        print(f"📥 Reading: {link}")
        combined_text += scrape_text(link) + "\n"

    summary = summarize_with_groq(combined_text, topic)
    print("\n📝 Summary:\n")
    print(summary)
    interactive_qna(summary, topic)

if __name__ == "__main__":
    main()
