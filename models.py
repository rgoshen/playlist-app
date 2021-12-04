"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()


playlists_songs = db.Table('playlists_songs',
                        db.Column('id', db.Integer, primary_key=True,
                                  autoincrement=True),
                        db.Column('playlist_id', db.Integer, db.ForeignKey(
                            'playlists.id', ondelete='cascade'), primary_key=True),
                        db.Column('song_id', db.Integer, db.ForeignKey(
                            'songs.id', ondelete='cascade'), primary_key=True)
                        )


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True
                   )
    name = db.Column(db.String(50),
                     nullable=False
                     )
    description = db.Column(db.String(100))
    songs = db.relationship('Song', secondary=playlists_songs,
                            backref=db.backref('playlists',lazy='dynamic'))


class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True
                   )
    title = db.Column(db.String(50),
                      nullable=False
                      )
    artist = db.Column(db.String(30))


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
