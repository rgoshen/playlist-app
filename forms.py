"""Forms for playlist app."""

from wtforms import SelectField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, Optional


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title', validators=[InputRequired(message='Please provide a song title'), Length(
        max=50, message='Cannot be more than 50 characters')])
    artist = StringField('Artist name', validators=[Length(
        max=30, message='can not be more than 30 characters'), Optional()])
    submit = SubmitField('Add')


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
