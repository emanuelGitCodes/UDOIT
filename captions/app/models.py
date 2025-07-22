from .extensions import db


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1024), nullable=False)
    captions = db.relationship("Caption", backref="video", lazy=True)


class Caption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey("video.id"), nullable=False)
    language = db.Column(db.String(20), nullable=False)
    path = db.Column(db.String(1024), nullable=False)
