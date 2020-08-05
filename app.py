from flask import Flask, render_template, url_for
from forms import PostForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '3543v5af7s5x1c6835a1x168d73xcsk'

@app.route('/')
@app.route('/home')
def home():
    title="Home"
    return render_template("home.html", title=title)

@app.route('/contact-us')
def contact_us():
    return render_template("contact.html")

@app.route('/login')
def first():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/background')
def background():
    return render_template('background.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add_post')
def add_post():
    form = PostForm()
    return render_template('add_post.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)