from flask import Flask, render_template
from config import Config
from forms import GithubUsernameForm


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def home_page():
    form = GithubUsernameForm()
    return render_template("home_page.html", form=form)


#this must be at the end of the page
if __name__ == "__main__":
    app.run(debug=True)
