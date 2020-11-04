
  
# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to a python function
@app.route('/')
def home():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("home.html")

from jinja2 import Template

def author1():
    greeting = "Hello!!"
    name = "Sriya Chilla"
    dob = "August 29"
    color = "Red"
    story = "story"
    info = {"greeting": greeting, "name": name, "dob": dob, "color": color, "story": story}
    return info

@app.route('/about')
def jinja():
    #function use Flask import (Jinja) to render an HTML template
    info = author1()
    tm = Template("my name is {{info.name}}.")
    return render_template(tm)

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='0.0.0.0')
    