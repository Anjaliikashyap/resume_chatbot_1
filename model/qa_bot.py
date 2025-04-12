from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer_question(context, question):
    result = qa_pipeline({'context': context, 'question': question})
    return result['answer']
