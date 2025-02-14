from flask import Flask, render_template, request
import requests
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('dictionary.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dictionary (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT NOT NULL,
                    meaning TEXT NOT NULL
                 )''')
    conn.commit()
    conn.close()

def get_api_meaning(word):
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
        return meaning
    else:
        return "Definition not found."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_meaning', methods=['POST'])
def get_word_meaning():
    word = request.form['word']
    meaning = get_api_meaning(word)

    conn = sqlite3.connect('dictionary.db')
    c = conn.cursor()
    c.execute("INSERT INTO dictionary (word, meaning) VALUES (?, ?)", (word, meaning))
    conn.commit()
    conn.close()

    return render_template('index.html', word=word, meaning=meaning)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

