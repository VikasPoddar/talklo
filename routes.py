from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route('/')
def home() :
    return render_template('home.htm')

@app.route('/contact')
def contact() :
    return render_template('contact.htm')

@app.route('/about')
def about() :
    return render_template('about.htm',message=' hello to this world ')

@app.route('/login')
def login() :
    return render_template('login.htm')

@app.route('/signup')
def signup() :
    return render_template('signup.htm')


if __name__=="__main__" :
    app.run()