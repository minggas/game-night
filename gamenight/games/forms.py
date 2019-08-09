from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class GameForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    time = IntegerField('Avg Time', validators=[DataRequired()])
    max_players = IntegerField('Max Players', validators=[DataRequired()])
    picture = FileField('Game Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Game')
