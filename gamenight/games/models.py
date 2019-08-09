from gamenight.shared.models import db

class Game(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	max_players = db.Column(db.Integer, nullable=False)
	time = db.Column(db.Integer, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	description = db.Column(db.Text, nullable=False)
	player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

	def __repr__(self):
		return '<Game %r>' % self.title