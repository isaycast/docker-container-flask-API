from ..extensions import db, ma
from app import app as app
from .Streets import StreetsSchema


class Streets_addresses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"))
    street_id = db.Column(db.Integer, db.ForeignKey("streets.id"))
    street = db.relationship(
        "Streets", backref="employees", lazy="select", uselist=False, cascade="delete"
    )

class Street_addressesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("street",)

    street = ma.Nested(StreetsSchema)
    