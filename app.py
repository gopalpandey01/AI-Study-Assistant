
import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load API key from local .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="centered"
)

# App title
st.title("📚 AI Study Assistant")
st.write("Ask a question and get an AI-generated explanation.")

# Question input
question = st.text_area(
    "Enter your study question:",
    placeholder="Example: Explain Data Analytics in simple words"
)

# Generate answer
if st.button("Get AI Answer"):
    if not question.strip():
        st.warning("Please enter a question.")

    else:
        # Get API key from environment or Streamlit Cloud Secrets
        api_key = os.getenv("GROQ_API_KEY")

        try:
            api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            pass

        if not api_key:
            st.error(
                "GROQ_API_KEY missing. "
                "Please configure your .env file or Streamlit Secrets."
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

                answer = response.choices[0].message.content

                st.subheader("Answer")
                st.markdown(answer)

            except Exception as e:
                st.error(f"Could not generate answer: {e}")
