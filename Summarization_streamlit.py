import streamlit as st
from transformers import pipeline

# Load pre-trained summarization pipeline
summarizer = pipeline("summarization")

# App title
st.title("Text Summarizer with Hugging Face Transformers")

# Text input
st.subheader("Enter Text to Summarize:")
text = st.text_area("Input your text here", height=200, 
                    placeholder="Paste the text you want to summarize.")

# Parameters for summarization
st.sidebar.header("Summary Parameters")
max_length = st.sidebar.slider("Max Length", 10, 100, 50, 1)
min_length = st.sidebar.slider("Min Length", 5, 50, 25, 1)
do_sample = st.sidebar.checkbox("Enable Sampling", value=False)

# Summarize button
if st.button("Summarize"):
    if not text.strip():
        st.warning("Please provide text for summarization.")
    else:
        with st.spinner("Generating summary..."):
            try:
                summary = summarizer(
                    text, max_length=max_length, min_length=min_length, do_sample=do_sample
                )
                st.subheader("Summarized Text:")
                st.success(summary[0]['summary_text'])
            except Exception as e:
                st.error(f"An error occurred: {e}")

