from app import db

class DonneeBoursiere(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    adj_close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return f'<DonneeBoursiere {self.date}>'
