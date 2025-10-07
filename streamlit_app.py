import streamlit as st
from translator import translate_text

st.set_page_config(page_title="AI Translation Engine", layout="wide")

st.title("🌐 AI Translation Engine")
st.write("Translate text between 200+ languages using NLLB or Hugging Face API.")

backend = st.sidebar.radio("Select Backend", ["Hugging Face Inference API", "Local Transformers"], index=0)
src_lang = st.selectbox("Source Language Code", ["eng_Latn", "hin_Deva", "fra_Latn", "spa_Latn"], index=0)
tgt_lang = st.selectbox("Target Language Code", ["hin_Deva", "eng_Latn", "fra_Latn", "spa_Latn"], index=1)

text_input = st.text_area("Enter text to translate:", height=150)
if st.button("Translate"):
    if text_input.strip():
        with st.spinner("Translating..."):
            translation = translate_text(text_input, src_lang, tgt_lang, backend)
            st.success("✅ Translation Complete!")
            st.text_area("Translated Text:", translation, height=150)
    else:
        st.warning("Please enter some text to translate.")