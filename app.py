from flask import Flask, render_template, request, redirect, url_for
import json
from db import load_poems, save_poem

app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/home')
def home():
    poems = load_poems()
    return render_template('index.html', poems=poems)

@app.route('/add', methods=['GET', 'POST'])
def add_poem():
    if request.method == 'POST':
        author = request.form.get('author', '').strip()
        show_name = request.form.get('show_name')
        title = request.form.get('title')
        content = request.form.get('content').strip()

        # If user doesn't want to show name or left it blank
        if not show_name or author == "":
            author = "Anonymous"

        new_poem = {
            "author": author,
            "title": title,
            "content": content
        }
        save_poem(new_poem)
        return redirect(url_for('home'))

    return render_template('add_poem.html')

    return render_template('add_poem.html')

@app.route('/view/<int:index>')
def view_poem(index):
    poems = load_poems()
    if 0 <= index < len(poems):
        poem = poems[index]
        return render_template('view_poems.html', poem=poem)
    return "Poem not found", 404

if __name__ == '__main__':
    app.run(debug=True)
