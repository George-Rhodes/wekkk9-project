from application import db



class ticket_prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.String(6), nullable=False)
    prize = db.Column(db.String(200), nullable=False)
    