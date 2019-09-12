from flask import Flask, render_template,url_for
from form import RegistrationForm,LoginForm
import requests



app = Flask(__name__)
app.config['SECRET_KEY']='af4c76322516d4273b7624476bf410ef'

posts=[
    {
        'author':'Nafish ',
        'title':'blog post 1',
        'content': 'first post content'
    },
    {
        'author':'ramiz raza',
        'title':'blog post 2',
        'content': 'Second post content'
    },
{
        'author':'saif raza',
        'title':'blog post 3',
        'content': 'Third post content'
    }
]

@app.route("/")
def boot():
    return render_template("bootstrap.html")
    
@app.route("/index")
def home():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)

if __name__ == '__main__':
	app.run(debug=True)
