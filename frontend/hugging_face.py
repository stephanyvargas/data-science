# hugging_face.py
import streamlit as st

def load_page():
    st.write("""
    ## Hugging Face Project

    **Hugging Face** is a company that offers a powerful, and ever-growing, library called Transformers that facilitates the use of many pre-trained models, especially ones tailored for Natural Language Processing (NLP).

    It has democratized the use of advanced models like BERT, GPT-2, and more. Their infrastructure and models are pivotal in the recent success and applicability of transfer learning in NLP.

    ### Some Relevant Notes:
    - The library provides interfaces for many popular machine learning frameworks such as TensorFlow and PyTorch.
    - Models can be easily loaded and used without much hassle, saving researchers and developers significant time.
    - The Hugging Face model hub also provides users the ability to share their pre-trained models.

    ### Sample Code:
    ```python
    from transformers import BertTokenizer, BertForSequenceClassification
    import torch

    # Load pre-trained model and tokenizer
    model_name = 'bert-base-uncased'
    model = BertForSequenceClassification.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)

    # Encode a sentence and predict
    inputs = tokenizer("Hugging Face is creating a tool that democratizes AI.", return_tensors="pt")
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    st.write(f"Prediction: {predictions}")
    ```
    """)


