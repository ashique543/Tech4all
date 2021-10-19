from flask import Flask, app
from flask.templating import render_template


app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",heading="Welcome to Tech4all your one source for all Tech")

@app.route('/Blog')
def blog():
    return render_template("blog.html", heading="Blog")

@app.route('/About')
def about():
    return render_template("about.html", heading="About Us")

@app.route('/Contact')
def contact():
    return render_template("contact.html", heading="Contact Us")

if __name__=='__main__':
    app.run(debug=True)