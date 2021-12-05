"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import InputRequired, Length, Optional


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Name', validators=[InputRequired(message='Please provide a playlist name'), Length(
        max=30, message='Cannot be more than 30 characters')])
    description = StringField('Description', validators=[Length(
        max=100, message='can not be more than 100 characters'), Optional()])
    submit = SubmitField('Add')


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title', validators=[InputRequired(message='Please provide a song title'), Length(
        max=30, message='Cannot be more than 30 characters')])
    artist = StringField('Artist name', validators=[Length(
        max=30, message='can not be more than 30 characters'), Optional()])
    submit = SubmitField('Add')


class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int, validators=[
                       InputRequired(message='Please select from the given list')])
    submit = SubmitField('Add')
