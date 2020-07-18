from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class InfoForm(FlaskForm):
    breed = StringField("de que raza eres: ")
    submit = SubmitField("Send")
