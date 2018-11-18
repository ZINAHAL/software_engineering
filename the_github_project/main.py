from flask import Flask, render_template, flash
from config import Config
from forms import GithubUsernameForm


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=["GET", "POST"])
def home_page():
    form = GithubUsernameForm()
    if form.validate_on_submit():
        flash("{}: Here is your pie...".format(form.username.data))

    return render_template("home_page.html", form=form)


#this must be at the end of the page
if __name__ == "__main__":
    app.run(debug=True)
