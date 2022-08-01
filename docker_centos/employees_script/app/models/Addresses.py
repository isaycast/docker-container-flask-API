from ..extensions import db, ma
from app import app as app
from .Cities_addresses import Cities_addressesSchema
from .States_addresses import States_addressesSchema

class Addresses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    zip_code = db.Column(db.String())
    employees_id = db.Column(db.Integer, db.ForeignKey("employees.id"))
    street = db.Column(db.String(1000))
    cities_addresses = db.relationship(
        "Cities_addresses", backref="employees", lazy="select", uselist=False, cascade="all, delete"
    )
    states_addresses = db.relationship(
        "States_addresses", backref="employees", lazy="select", uselist=False, cascade="all, delete"
    )
    


    def __init__ (self, zip_code, street):
       
        self.zip_code = zip_code
        self.street = street

class AddressSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = (
                 "zip_code",
                 "street",
                 "cities_addresses.cities.city_name", 
                 "states_addresses.states.state_name")

    cities_addresses = ma.Nested(Cities_addressesSchema)
    states_addresses = ma.Nested(States_addressesSchema)