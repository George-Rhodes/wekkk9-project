from application import db

class ticks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_num = db.Column(db.String(6), nullable=False)
    prize_info = db.Column(db.String(200), nullable=False)
    