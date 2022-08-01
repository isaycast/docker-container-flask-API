from ..extensions import db, ma

from app import app as app

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    city_name = db.Column(db.String(), unique=True)

    def __init__ (self, city_name):
        self.city_name = city_name

class CitiesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("city_name",)
