from .models.Cities import Cities
from .models.States import States
from .models.Companies import Companies
from .models.Departaments import Departaments

class ValidationAddress():
    def __init__ (self, db):
        self.db = db
        self.cities_dic = {}
        self.states_dic = {}
        self.companies_dic = {}
        self.departament_dic = {}
    
    def get_dictionaries(self):
        self.cities_dic = {city_obj.city_name:city_obj  for city_obj in self.db.session.query(Cities).all()}
        self.states_dic = {state_obj.state_name:state_obj  for state_obj in self.db.session.query(States).all()}
        self.companies_dic = {company_obj.company_name:company_obj  for company_obj in self.db.session.query(Companies).all()}
        self.departament_dic = {dpto_obj.departament_name:dpto_obj  for dpto_obj in self.db.session.query(Departaments).all()}
    
    def it_empy(self):
        return not self.cities_dic