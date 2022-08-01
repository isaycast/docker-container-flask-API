from app import app
from .extensions import db
from .models.Contacts import Contacts
from .models.Employees import Employees, EmployeesSchema
from .models.Addresses import Addresses
from .models.Cities import Cities
from .models.Cities_addresses import Cities_addresses
from .models.States import States
from .models.States_addresses import States_addresses
from .models.Companies import Companies
from .models.Employees_companies import Employees_companies
from .models.Departaments import Departaments


employee_schema = EmployeesSchema()
employees_schema = EmployeesSchema(many=True)



def createTables():
    db.create_all()

def add_data(first_name, second_name, phone1, phone2, email, streetAddress, zip_code, city, state, company, departament):
    employ = Employees(first_name, second_name)
    contact = Contacts(phone1, phone2, email)
    address = Addresses(zip_code, streetAddress)
    city = Cities(city)
    state = States(state)
    company = Companies(company)
    
    



    state_addresses = States_addresses()
    city_addresses = Cities_addresses()
    employee_company = Employees_companies()
  

    employ.contact = contact
    employee_company.companies = company
    employ.employees_companies = employee_company

    state_addresses.states = state
    address.states_addresses = state_addresses
    
    city_addresses.cities = city
    address.cities_addresses = city_addresses
    employ.address = address
    

    db.session.add(employ)
    db.session.add(contact)
    db.session.add(address)
    
    db.session.add(city)
    db.session.add(city_addresses)
    db.session.add(state)
    db.session.add(state_addresses)
    db.session.add(company)
    db.session.add(employee_company)

    db.session.commit()


@app.route('/')
def main_index():
    """
    Home give instructions to use API
    """
    return "Welcome to employees API there are to endpoints /read (read all users in db) /delete/<id> (delete user from id)"


@app.route('/read')
def read_employees():
    """
    Read all employees from database
    """
    employees = db.session.query(Employees).all()
    
    return {"employees":employees_schema.dump(employees)}

@app.route('/delete/<int:id>', methods=["DELETE"])
def delete_employee(id):
    """
    Delete employ from database

    Keyword arguments:
    id -- The id is give from API endpoint
    """
    employee_to_delete = Employees.query.get(id)
    if not employee_to_delete:
        return {"messagge":"employee not in database"}
    db.session.delete(employee_to_delete)
    db.session.commit()
    return {"message":"success delete"}

@app.errorhandler(404) 
def invalid_route(e): 
    """
    Manage errors paths
    """
    return "Invalid route pleas use /read or /delete/<id>."

# @app.route('/create', methods=["GET"])
# def add_employee():
#     add_data()
#     return {"message": "success added"}

# @app.route('/createTable', methods=["GET"])
# def create_tables():
#     createTables()
#     return {"message": "success created"}