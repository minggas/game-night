from gamenight.shared.models import db

class Player(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  games = db.relationship('Game', backref='owner', lazy=True)

  def __repr__(self):
    return '<Player %r>' % self.name