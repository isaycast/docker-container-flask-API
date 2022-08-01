from ..extensions import db, ma

from app import app as app

class Streets(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    street_name = db.Column(db.String(), unique=True)

    def __init__ (self, street_name):
        self.street_name = street_name

class StreetsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("street_name",)
