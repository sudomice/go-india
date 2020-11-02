from app import db
from sqlalchemy.dialects.postgresql import BOOLEAN


class Result(db.Model):
    __tablename__ = 'results'

    code = db.Column(db.String(), primary_key=True)
    destination = db.Column(db.String())
    claimed = db.Column(BOOLEAN)

    def __init__(self, code, destination, claimed):
        self.code = code
        self.destination = destination
        self.claimed = claimed

    def __repr__(self):
        return '<code {}>'.format(self.code)