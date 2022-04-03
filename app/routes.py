from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Arsenii'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Lviv!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Arsenii'},
            'body': 'It works!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)