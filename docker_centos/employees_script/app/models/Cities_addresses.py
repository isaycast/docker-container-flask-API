from ..extensions import db, ma
from app import app as app
from .Cities import CitiesSchema


class Cities_addresses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"))
    cities_id = db.Column(db.Integer, db.ForeignKey("cities.id"))
    cities = db.relationship(
        "Cities", backref="employees", lazy="select", uselist=False
    )

class Cities_addressesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("cities",)

    cities = ma.Nested(CitiesSchema)
    