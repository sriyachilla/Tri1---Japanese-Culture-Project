
  
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

from jinja2 import Template

@app.route('/social_structure')
def social_structure():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("socialstructure.html")

@app.route('/art')
def art():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("art.html")

@app.route('/food')
def food():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("food.html")

@app.route('/traditions')
def traditions():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("traditions.html")

@app.route('/history')
def history():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("history.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='127.0.0.1')
    