from . import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Egor'}
    posts = [
        {'author': {'username': 'Jonh'},
         'body': 'Beatifull day in Belarus!'
         },
        {'author': {'username': 'Susan'},
         'body': 'The Avengers movie was so cool!'
         }

    ]
    return render_template('index.html', title="Home", user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sing In', form=form)
