
  
# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to a python function
@app.route('/')
@app.route('/home')
def home():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("home.html")

#from jinja2 import Template

@app.route('/social_structure')
def social_structure():
    posts = [{'title': 'SOCIAL STRUCTURE', 'author': 'Quentin Chong'}]
    #function use Flask import (Jinja) to render an HTML template
    return render_template("socialstructure.html", posts=posts)

@app.route('/art')
def art():
    posts = [{'title': 'ART', 'author': 'Sam Mahjouri', 'summary': 'The development of Japanese Art Styles --- ANIME'}]
    #function use Flask import (Jinja) to render an HTML template
    return render_template("art.html", posts=posts)

@app.route('/food')
def food():
    posts = [{'title': 'FOOD', 'author': 'Bryce Modugno', 'summary': 'Japanese Foods and Traditional Preparation'}]
    #function use Flask import (Jinja) to render an HTML template
    return render_template("food.html", posts=posts)

@app.route('/traditions')
def traditions():
    posts = [{'title': 'TRADITIONS', 'author': 'Francis Lim', 'summary': ''}]
    #function use Flask import (Jinja) to render an HTML template
    return render_template("traditions.html", posts=posts)

@app.route('/history')
def history():
    posts = [{'title': 'HISTORY', 'author': 'Quentin Chong', 'summary': 'The history of Japan from its Ancient Times'}]
    #function use Flask import (Jinja) to render an HTML template
    return render_template("history.html", posts=posts)

@app.route('/testknowledgegame')
def testknowledgegame():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("testknowledgegame.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='127.0.0.1')
    