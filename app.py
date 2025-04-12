from flask import Flask, request, render_template
from model.extractor import extract_text_from_pdf, extract_text_from_docx
from model.qa_bot import answer_question
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
context = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global context
    if request.method == 'POST':
        file = request.files['resume']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        if file.filename.endswith(".pdf"):
            context = extract_text_from_pdf(path)
        elif file.filename.endswith(".docx"):
            context = extract_text_from_docx(path)
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    global context
    question = request.form['question']
    answer = answer_question(context, question)
    return {'answer': answer}

if __name__ == '__main__':
    app.run(debug=True)
