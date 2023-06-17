from flask import Flask, render_template, request
from model import query

app = Flask(__name__)

# Topics
topics = [
    "Ant",
    "Cougar",
    "Koala",
    "Giant Panda",
    "Lobster",
    "Butterfly",
    "Dragonfly",
    "Eel",
    "Zebra",
    "Octopus"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        answer = query(question)
        return render_template('index.html', topics=topics, answer=answer)
    return render_template('index.html', topics=topics)

if __name__ == '__main__':
    app.run(debug=True)
