import streamlit as st
from PIL import Image
import pytesseract
from transformers import pipeline

st.set_page_config(page_title="Social Media Summarizer", page_icon="📱", layout="wide")

@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

def summarize_text(text: str, max_length: int = 120, min_length: int = 30) -> str:
    text = text.strip()
    if not text:
        raise ValueError("Text is empty.")
    if len(text.split()) < 10:
        return "Text is too short to summarize meaningfully."

    model = load_model()
    result = model(text, max_length=max_length, min_length=min_length, do_sample=False)
    return result[0]["summary_text"]

def summarize_image(image_file) -> dict:
    image = Image.open(image_file)
    if image.mode in ("RGBA", "LA", "P"):
        image = image.convert("RGB")

    extracted = pytesseract.image_to_string(image).strip()
    if not extracted:
        raise ValueError("No text was detected in the image.")

    summary = summarize_text(extracted)
    return {
        "extracted_text": extracted,
        "summary": summary
    }

st.title("📱 Social Media Summarizer")
st.markdown("Summarize text posts or image-based social posts using a free local model.")

tab1, tab2 = st.tabs(["Text Post", "Image Post"])

with tab1:
    text = st.text_area("Paste post text", height=220)
    if st.button("Summarize Text"):
        if text:
            try:
                summary = summarize_text(text)
                st.success("Summary")
                st.write(summary)
            except Exception as e:
                st.error(str(e))
        else:
            st.warning("Please enter text.")

with tab2:
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        if st.button("Extract and Summarize"):
            try:
                result = summarize_image(uploaded_file)
                st.image(uploaded_file, caption="Uploaded image", use_column_width=True)

                st.success("Extracted text")
                st.write(result["extracted_text"])

                st.success("Summary")
                st.write(result["summary"])
            except Exception as e:
                st.error(str(e))
