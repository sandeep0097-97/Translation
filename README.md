# 🌐 Streamlit Translation Engine

Translate text between 200+ languages using Meta's **NLLB (No Language Left Behind)** model.

## 🚀 Features
- Supports **local model inference** or **Hugging Face Inference API**
- Built with **Streamlit + Transformers**
- Deployable on **Streamlit Cloud**

## 🧩 Setup
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 🔑 Hugging Face API (for Streamlit Cloud)
1. Go to [Hugging Face Tokens](https://huggingface.co/settings/tokens)
2. Create a token and add it to Streamlit Cloud Secrets:
```
HF_API_TOKEN = "your_token_here"
```

## 🛰️ Deployment
Push this repo to GitHub and deploy directly on [Streamlit Cloud](https://share.streamlit.io/).

## ⚙️ Example
```python
from translator import translate_text
translate_text("Hello!", "eng_Latn", "hin_Deva")
```

## 📜 License
MIT License © 2025
