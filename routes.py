from flask import Flask
from flask.templating import render_template

app=Flask(__name__)

@app.route('/')
def home() :
    return render_template('home.htm')


app.run(debug=1)