import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

# Paste your Gemini API key here
genai.configure(api_key="AIzaSyDczN7OIw1W2V2exjsHWBSNcLge3NZMKLc")

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("📄 Chat with Your Notes")

pdf = st.file_uploader("Upload a PDF file", type="pdf")

if pdf is not None:
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    st.success("✅ PDF loaded!")

    question = st.text_input("Ask a question about the notes:")

    if question:
        with st.spinner("Generating answer..."):
            response = model.generate_content(f"Notes:\n{text}\n\nQuestion: {question}")
            st.write("### Answer:")
            st.write(response.text)
