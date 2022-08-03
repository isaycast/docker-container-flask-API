from ..extensions import db, ma
from app import app as app
from .Companies import CompaniesSchema


class Employees_companies(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    employees_id = db.Column(db.Integer, db.ForeignKey("employees.id"))
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    companies = db.relationship(
        "Companies", backref="employees", lazy="select", uselist=False
    )

class Employees_companiesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("companies",)

    companies = ma.Nested(CompaniesSchema)