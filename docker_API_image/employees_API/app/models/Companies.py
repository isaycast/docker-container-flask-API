from ..extensions import db, ma

from app import app as app

class Companies(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    company_name = db.Column(db.String(), unique=True)

    def __init__ (self, company_name):
        self.company_name = company_name

class CompaniesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("company_name",)