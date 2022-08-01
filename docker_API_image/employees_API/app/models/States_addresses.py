from ..extensions import db, ma
from app import app as app
from .States import StatesSchema


class States_addresses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"))
    states_id = db.Column(db.Integer, db.ForeignKey("states.id"))
    states = db.relationship(
        "States", backref="employees", lazy="select", uselist=False
    )

class States_addressesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("states",)

    states = ma.Nested(StatesSchema)