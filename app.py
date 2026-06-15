import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
st.title("API Response Explainer")
st.caption("Paste any API response and get a plain-English breakdown")
#sample API responses
input = ""
option = st.selectbox(
    "Choose Sample responses to see the behaviour",
    [
      '{"tax_amt":12,"total_due":123,"total_item_count":2,"updated_at":"2026-03-10 10:05:16","weight":0.0000}',
      '{"base_grand_total": 123,"base_total_due": 0,"billing_address_id": 4827,"created_at": "2026-03-10 10:05:16","customer_email": "abc@gmail.com"}',
      'I have my own payload'
    ]
)
if option == 'I have my own payload':
    input = st.text_area("API Payload", "", height=300)
else:
    input = st.text_area("API Payload", option, height=300)

def get_llm_response(query):
    # print(os.getenv("GROQ_API_KEY"))
    # return "hi"
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "Please set the GROQ_API_KEY environment variable."
    groq = Groq(
        api_key=api_key
    )
    response = groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system", "content": "You are a heplful assisstant to explain the API responses"},
            {"role":"user", "content": "Explain individual fields and also provide a final summary on which are important ones useful for development with some usecases"},
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message.content
button = st.button("Explain")
if button and input:
    with st.spinner("Analyzing..."):
        try:
            explanation = get_llm_response(input)
            st.markdown(explanation)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
elif button and not input:
    st.warning("Please paste an API response first")