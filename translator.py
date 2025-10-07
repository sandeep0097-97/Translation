import os
from transformers import pipeline
import torch
import requests

def translate_text(text, src_lang, tgt_lang, backend="Hugging Face Inference API"):
    if backend == "Local Transformers":
        try:
            translator = pipeline(
                task="translation",
                model="facebook/nllb-200-distilled-600M",
                torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32
            )
            result = translator(text, src_lang=src_lang, tgt_lang=tgt_lang)
            return result[0]['translation_text']
        except Exception as e:
            return f"Error loading local model: {str(e)}"
    else:
        token = os.getenv("HF_API_TOKEN", None)
        if not token:
            return "Missing Hugging Face API token. Add it to Streamlit Secrets or env vars."
        headers = {"Authorization": f"Bearer {token}"}
        payload = {
            "inputs": text,
            "parameters": {"src_lang": src_lang, "tgt_lang": tgt_lang}
        }
        response = requests.post(
            "https://api-inference.huggingface.co/models/facebook/nllb-200-distilled-600M",
            headers=headers, json=payload
        )
        if response.status_code == 200:
            return response.json()[0]['translation_text']
        return f"API Error: {response.text}"