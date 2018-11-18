from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField

class GithubUsernameForm(FlaskForm):
    username = TextField()
    submit_button = SubmitField("Submit")

