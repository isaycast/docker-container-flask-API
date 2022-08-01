
from app.models.Departaments import DepartamentsSchema
from ..extensions import db, ma
from app import app as app
from .Contacts import ContactsSchema
from .Addresses import AddressSchema
from .Employees_companies import Employees_companiesSchema



employees_departaments = db.Table(
    "employees_departaments",
    db.Column("employee_id", db.Integer, db.ForeignKey("employees.id")),
    db.Column("departament_id", db.Integer, db.ForeignKey("departaments.id")),
)

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(120))
    contact = db.relationship(
        "Contacts", backref="employees", lazy="select", uselist=False, cascade="all, delete"
    )
    address = db.relationship(
        "Addresses", backref="employees", lazy="select", uselist=False, cascade="all, delete"
    )

    employees_companies = db.relationship(
        "Employees_companies", backref="employees", lazy="select", uselist=False, cascade="all, delete"
    )
    departaments = db.relationship(
        "Departaments", backref="employees", lazy="select", secondary = employees_departaments, cascade="all, delete"
    )

    

    def __init__ (self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class EmployeesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", 
                "firstname", 
                "lastname",
                 "contact", 
                 "address",
                 "employees_companies.companies.company_name",
                 "departaments")
                 #"employees_departaments.departaments.departament_name",)

    contact = ma.Nested(ContactsSchema)
    address = ma.Nested(AddressSchema)
    employees_companies = ma.Nested(Employees_companiesSchema)
    departaments = ma.Nested(DepartamentsSchema(many=True))