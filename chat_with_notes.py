
import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai

st.set_page_config(page_title="Chat with Your Notes 🤖")

st.title("📄 Chat with Your PDF Notes (Gemini)")

# Ask for API Key
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")

# Upload PDF
uploaded_file = st.file_uploader("📤 Upload your PDF file", type="pdf")

# Ask question
question = st.text_input("❓ Ask a question about the PDF")

if uploaded_file and api_key and question:
    try:
        genai.configure(api_key=api_key)
        
        # ✅ Use Gemini 1.5 Flash here
        model = genai.GenerativeModel("gemini-1.5-flash")

        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            pdf_text = "\n".join([page.get_text() for page in doc])

        prompt = f"My notes:\n\n{pdf_text}\n\nQuestion: {question}"
        response = model.generate_content(prompt)

        st.success("✅ Answer:")
        st.write(response.text)

    except Exception as e:
        st.error(f"Error: {e}")
