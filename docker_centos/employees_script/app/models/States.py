from ..extensions import db, ma

from app import app as app

class States(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    state_name = db.Column(db.String(), unique=True)

    def __init__ (self, state_name):
        self.state_name = state_name

class StatesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("state_name",)
