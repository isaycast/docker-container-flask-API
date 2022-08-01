from ..extensions import db, ma

from app import app as app

class Departaments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    departament_name = db.Column(db.String(), unique=True)

    def __init__ (self, departament_name):
        self.departament_name = departament_name

class DepartamentsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("departament_name",)