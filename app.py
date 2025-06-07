import streamlit as st
from scraper import get_search_links
from summarizer import scrape_text, summarize_with_groq

st.set_page_config(page_title="AI Mini Knowledge", layout="wide")
st.title("🧠 AI Mini Knowledge")
st.write("Get detailed summaries and ask follow-up questions on any topic.")


if "summary_history" not in st.session_state:
    st.session_state.summary_history = []
if "qa_history" not in st.session_state:
    st.session_state.qa_history = []


with st.form("summarize_form"):
    topic = st.text_input("🔍 Enter your topic:")
    submitted = st.form_submit_button("Summarize")

    if submitted and topic:
        with st.spinner("Fetching and summarizing..."):
            links = get_search_links(topic)
            combined_text = ""
            for link in links:
                combined_text += scrape_text(link) + "\n"

            summary = summarize_with_groq(combined_text, topic)

            st.session_state.summary_history.append({
                "topic": topic,
                "summary": summary
            })
            st.session_state.current_topic = topic  # for Q&A
            st.session_state.current_summary = summary


if st.session_state.summary_history:
    st.subheader("📝 Summary ")
    for item in reversed(st.session_state.summary_history):
        st.markdown(f"#### 📌 {item['topic']}")
        st.markdown(item['summary'])


if "current_summary" in st.session_state:
    with st.form("qa_form"):
        question = st.text_input("❓ Ask a follow-up question about the topic:")
        ask_submitted = st.form_submit_button("Ask")

        if ask_submitted and question:
            with st.spinner("Thinking..."):
                followup_prompt = (
                    f"Topic: {st.session_state.current_topic}\n\n"
                    f"Summary:\n{st.session_state.current_summary}\n\n"
                    f"Follow-up question:\n{question}"
                )
                answer = summarize_with_groq(followup_prompt, st.session_state.current_topic)
                st.session_state.qa_history.append({
                    "question": question,
                    "answer": answer
                })

# --- Show Q&A History ---
if st.session_state.qa_history:
    st.subheader("📚 Follow-up Q&A History")
    for item in reversed(st.session_state.qa_history):
        st.markdown(f"**Q:** {item['question']}")
        st.markdown(f"**A:** {item['answer']}")
        st.markdown("---")