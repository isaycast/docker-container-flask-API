from app import app
from flask import  request
from .ValidationAddress import ValidationAddress
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


validationAddress = ValidationAddress(db)
employee_schema = EmployeesSchema()
employees_schema = EmployeesSchema(many=True)


 

def create_employee(first_name, last_name, phone1, phone2, email, streetAddress, zip_code, city, state, company, departaments):
    """
    Record a new employee in database

    Keyword arguments:
    first_name -- the first name of employee
    last_name -- the last_name name of employee
    phone1 -- primary phone
    phone2 -- secondary phone
    email -- email of employee
    streetAddress -- Street name where employee have they address
    zip_code -- Zip code address
    city -- Name of the city where employee lives
    state -- Name of the state where employee lives
    company -- Name of the company where employee belons
    departaments -- Array of departaments where empleeye belongs

    """
    # Creating objects
    employee = Employees(first_name, last_name)
    contact = Contacts(phone1, phone2, email)
    address = Addresses(zip_code, streetAddress)
    state_addresses = States_addresses()
    city_addresses = Cities_addresses()
    employee_company = Employees_companies()
    
    if validationAddress.it_empy():
        validationAddress.get_dictionaries()

    # If not is register in db the object is registered and append to list of object registered in db

    if city not in validationAddress.cities_dic.keys():
        city_obj = Cities(city)
        db.session.add(city_obj)
        validationAddress.cities_dic[city] = city_obj
    
    if state not in validationAddress.states_dic.keys():
        state_obj = States(state)
        db.session.add(state_obj)
        validationAddress.states_dic[state] = state_obj

    if company not in validationAddress.companies_dic.keys():
        company_obj = Companies(company)
        db.session.add(company_obj)
        validationAddress.companies_dic[company] = company_obj

    for departament in departaments:

        if departament not in  validationAddress.departament_dic.keys():
            depto_obj = Departaments(departament)
            db.session.add(depto_obj)
            validationAddress.departament_dic[departament] = depto_obj
        employee.departaments.append(validationAddress.departament_dic[departament])

    
    # Creating relations between objects
    employee.contact = contact
    employee_company.companies = validationAddress.companies_dic[company]
    employee.employees_companies = employee_company

    state_addresses.states = validationAddress.states_dic[state]
    address.states_addresses = state_addresses
    
    city_addresses.cities = validationAddress.cities_dic[city]
    address.cities_addresses = city_addresses
    employee.address = address
    
    # Adding object to db 
    db.session.add(employee)
    db.session.add(contact)
    db.session.add(address)
    db.session.add(city_addresses)
    db.session.add(state_addresses)
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

@app.route('/read/<name>')
def employees_by_name(name):
    """
    Read employees by first name

    Keyword arguments:
    name -- the first name of employee

    return -- list of employees that match with firstname
    """
    
    employees = db.session.query(Employees).filter_by(firstname = name)
    
    return {"employees":employees_schema.dump(employees)}

@app.route('/create', methods=["POST"])
def create_new_employee():
        data = request.get_json(force=True)
        first_name = data.get('first_name','')
        last_name = data.get('last_name','')
        phone1 = data.get('phone1','')
        phone2 = data.get('phone2','')
        email = data.get('email','')
        streetAddress = data.get('streetAddress','')
        zip_code = data.get('zip_code','')
        city = data.get('city','')
        state = data.get('state','')
        company = data.get('company','')
        departaments = data.get('departaments',[])
        
        create_employee(first_name, last_name, phone1, phone2, email, streetAddress, zip_code, city, state, company, departaments)
        
        return {"msg": "Created Succesfuly" }
     


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