from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title="Home"
    return render_template("home.html", title=title)

@app.route('/contact-us')
def contact_us():
    return render_template("contact.html")

@app.route('/login')
def first():
    return render_template("login.html")

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/background')
def background():
    return render_template('background.html')

if __name__ == '__main__':
    app.run(debug=True)