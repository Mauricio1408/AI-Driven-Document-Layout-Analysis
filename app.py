import streamlit as st

# --- Gemini API Setup ---
import google.generativeai as genai

# Set your Gemini API key here
GEMINI_API_KEY = "AIzaSyCZdSnnU912rFrP5l-7oWQELE2F1DC-MAs"
genai.configure(api_key=GEMINI_API_KEY)

# --- Helper Functions ---
import pdfplumber
from PIL import Image
import pytesseract
import cv2
import numpy as np
import pandas as pd
import json
import requests

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        return text

def extract_text_from_image(file):
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    return text

def extract_tables_from_pdf(file):
    tables = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            tables += page.extract_tables()
    return tables

def gemini_extract_fields(text, custom_fields):
    api_key = GEMINI_API_KEY
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    prompt = (
        f"Extract the following fields from this document: {', '.join(custom_fields)}. "
        "Return the result as a JSON object with field names as keys. "
        "If a field is not found, use null. Here is the document text:\n\n"
        f"{text}"
    )
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        candidates = response.json().get("candidates", [])
        if candidates:
            return candidates[0]["content"]["parts"][0]["text"]
        else:
            return "{}"
    else:
        return f"Error: {response.status_code} - {response.text}"
    
# --- Streamlit App with Pages ---
st.set_page_config(page_title="AI-Driven Document Layout Analysis", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ("Introduction", "Methodology", "Demo", "Feedback")
)

if page == "Introduction":
    st.title("AI-Driven Document Layout Analysis & Information Extraction")
    st.markdown("""
    Welcome to the AI-Driven Document Layout Analysis & Information Extraction app!  
    This tool allows you to upload complex documents (invoices, forms, reports) and uses advanced AI to:
    - Analyze document layout and structure
    - Extract key information (like invoice numbers, customer names, totals)
    - Organize the extracted data into structured formats (JSON, CSV)
    - Let you review and correct the results

    **Navigate using the sidebar to learn more, try the demo, or leave feedback!**
    """)

elif page == "Methodology":
    st.title("Methodology")
    st.markdown("""
    ### How does this app work?
    1. **Document Upload:** You upload a PDF or image file.
    2. **Layout Analysis:** The app uses PDF/image processing and OCR (Optical Character Recognition) to extract text and tables.
    3. **AI Extraction:** The extracted text is sent to Google's Gemini AI, which identifies and extracts the fields you specify.
    4. **User Review:** You can review, edit, and download the extracted data.
    5. **Feedback:** Your feedback helps us improve the system!

    **Technologies Used:**
    - `pdfplumber` and `pytesseract` for text and table extraction
    - `Gemini` (Google Generative AI) for intelligent information extraction
    - `Streamlit` for the interactive web interface
    """)

elif page == "Demo":
    st.title("Demo: Try the Document Analyzer")
    st.caption("Upload a PDF or image. The AI will extract the fields you specify. You can review and download the results.")

    uploaded_file = st.file_uploader("Upload a PDF or Image", type=["pdf", "png", "jpg", "jpeg"])
    if uploaded_file:
        st.success("File uploaded successfully!")
        file_type = uploaded_file.type
        if file_type == "application/pdf":
            st.caption("Previewing first page of PDF (if possible)...")
            try:
                with pdfplumber.open(uploaded_file) as pdf:
                    first_page = pdf.pages[0]
                    st.image(first_page.to_image(resolution=150).original, caption="First page preview")
            except Exception:
                st.warning("Could not preview PDF page.")
        else:
            st.image(uploaded_file, caption="Uploaded Image Preview")

        st.markdown("#### Step 1: Specify Fields to Extract")
        custom_fields = st.text_input(
            "Enter fields to extract (comma separated)",
            "invoice number, customer name, total amount"
        )
        st.caption("Example: invoice number, customer name, total amount")

        if st.button("Extract Data"):
            st.info("Extracting text from document...")
            if file_type == "application/pdf":
                text = extract_text_from_pdf(uploaded_file)
            else:
                text = extract_text_from_image(uploaded_file)
            st.success("Text extraction complete.")

            st.info("Sending extracted text to Gemini for information extraction...")
            extracted_json_str = gemini_extract_fields(text, [f.strip() for f in custom_fields.split(",")])
            try:
                extracted_json = json.loads(extracted_json_str)
            except Exception:
                st.warning("Could not parse Gemini response as JSON. Showing raw output.")
                st.code(extracted_json_str)
                extracted_json = None

            if extracted_json:
                st.markdown("#### Step 2: Review and Edit Extracted Data")
                edited_data = {}
                for key, value in extracted_json.items():
                    edited_data[key] = st.text_input(f"{key}", value if value is not None else "")
                st.markdown("#### Step 3: Download Results")
                df = pd.DataFrame([edited_data])
                st.download_button("Download as CSV", df.to_csv(index=False), "extracted_data.csv")
                st.download_button("Download as JSON", json.dumps(edited_data, indent=2), "extracted_data.json")
            else:
                st.info("Please review the raw output above.")

    else:
        st.info("Please upload a PDF or image to get started.")

elif page == "Feedback":
    st.title("Feedback")
    st.markdown("""
    We value your feedback! Please let us know your thoughts, suggestions, or any issues you encountered.
    """)

    # 5-star rating system
    st.markdown("#### How satisfied are you with this app?")
    satisfaction = st.radio(
        "Your rating:",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: "⭐" * x,
        horizontal=True,
        index=4
    )
    st.caption(f"You rated: {'⭐' * satisfaction}")

    feedback = st.text_area("Additional feedback")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")
        st.write(f"Your rating: {'⭐' * satisfaction}")
        if feedback.strip():
            st.write("Your comments:")
            st.write(feedback)