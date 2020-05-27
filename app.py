from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact-us')
def contact_us():
    return render_template("contact.html")

@app.route('/first')
def first():
    return render_template("first.html")

if __name__ == '__main__':
    app.run(debug=True)