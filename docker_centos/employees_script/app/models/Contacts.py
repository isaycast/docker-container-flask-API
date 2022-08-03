from ..extensions import db, ma

from app import app as app

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstphonne = db.Column(db.String())
    secondaryphone = db.Column(db.String())
    email = db.Column(db.String(100))
    employees_id = db.Column(db.Integer, db.ForeignKey("employees.id"))

    def __init__ (self, firstphonne, secondaryphone, email):
        self.firstphonne = firstphonne
        self.secondaryphone = secondaryphone
        self.email = email

class ContactsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("firstphonne", "secondaryphone", "email")