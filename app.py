
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("📚 AI Study Assistant")
st.write("Ask a question and get an AI-generated explanation.")

question = st.text_area(
    "Enter your study question:",
    placeholder="Example: Explain Data Analytics in simple words"
)

if st.button("Get AI Answer"):
    if not question.strip():
        st.warning("Please enter a question.")

    else:
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            st.error(
                "GROQ_API_KEY missing. Check your .env file."
            )
        else:
            try:
                client = Groq(api_key=api_key)

                with st.spinner("Generating your answer..."):
                    response = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are a helpful study assistant. "
                                    "Explain academic topics in simple "
                                    "language with headings and examples."
                                )
                            },
                            {
                                "role": "user",
                                "content": question
                            }
                        ]
                    )

                st.subheader("Answer")
                st.markdown(
                    response.choices[0].message.content
                )

            except Exception as e:
                st.error(f"Could not generate answer: {e}")
import os
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("GROQ_API_KEY")

print("API key loaded:", bool(api_key))
print("API key length:", len(api_key) if api_key else 0)