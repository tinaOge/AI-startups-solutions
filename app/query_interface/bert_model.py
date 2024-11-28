# app/query_interface/bert_model.py
import torch
from transformers import pipeline

device = torch.device("cpu")
# Load a BERT-based question-answering pipeline
qa_pipeline = pipeline("question-answering", model="deepset/bert-base-cased-squad2",device=device)

def get_kpi_answer(context, question):
    response = qa_pipeline(question=question, context=context)
    return response['answer']

# Example Usage
context = "Tech Innovators' revenue is $100,000, expenses are $50,000, and profit margin is 50%."
question = "What is the profit margin for Tech Innovators?"
print(get_kpi_answer(context, question))



