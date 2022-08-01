
import pandas as pd

from .extensions import db
from .models.Contacts import Contacts
from .models.Employees import Employees
from .models.Addresses import Addresses
from .models.Cities import Cities
from .models.Cities_addresses import Cities_addresses
from .models.States import States
from .models.States_addresses import States_addresses
from .models.Companies import Companies
from .models.Employees_companies import Employees_companies
from .models.Departaments import Departaments



def createTables():
    """
    Create tables in database
    """
    db.drop_all()
    db.create_all()
    

def populate_table():
    """
    Populate table based on csv proposed by company
    """
    # List variables to check if the city, state, company and departament already exist in database
    city = {}
    state = {}
    company = {}
    departaments = {}

    # Read sample as pandas dataframe
    sample_df = pd.read_csv("./employees_script/app/data/sample.csv") 
    # Divide employees with two departaments 
    two_departaments_data = sample_df[sample_df.duplicated(subset="first_name", keep=False)] 
    simple_data =  sample_df[~sample_df.duplicated(subset="first_name", keep=False)]

    # convert dataframe to Dic
    simple_data_dictionary = simple_data.to_dict(orient='records')
    # iter over dict to populate table
    for obj in simple_data_dictionary:
        employee = Employees(firstname=obj["first_name"], lastname=obj["last_name"])
        contact = Contacts(firstphonne=obj["phone1"], secondaryphone=obj["phone2"], email=obj["email"])
        address = Addresses(zip_code=obj["zip"], street=obj["address"])

        state_addresses = States_addresses()
        city_addresses = Cities_addresses()
        employee_company = Employees_companies()

        # Check if city, state, company or departament exist in previus insertions if not are added to database
        if obj["city"] not in city.keys() :
            city[obj["city"]] = Cities(obj["city"])
            db.session.add(city[obj["city"]])
        if obj["state"] not in state.keys() :
            state[obj["state"]] = States(obj["state"])
            db.session.add(state[obj["state"]])
        if  obj["company_name"] not in company.keys() :
            company[ obj["company_name"]] = Companies(obj["company_name"])
            db.session.add(company[obj["company_name"]] )
        if  obj["department"] not in departaments.keys() :
            departaments[obj["department"]] = Departaments(obj["department"])
            db.session.add(departaments[obj["department"]])

        # adding relation and information to db
        employee.departaments.append(departaments[obj["department"]])
        employee.contact = contact
        employee_company.companies =   company[ obj["company_name"]]
        employee.employees_companies = employee_company

        state_addresses.states =  state[obj["state"]]
        address.states_addresses = state_addresses
        
        city_addresses.cities =  city[obj["city"]]
        address.cities_addresses = city_addresses
        employee.address = address

        db.session.add(employee)
        db.session.add(contact)
        db.session.add(address)
        db.session.add(city_addresses)
        db.session.add(state_addresses)
        db.session.add(employee_company)
        db.session.commit()

    # drop duplicate to iter in 
    only_employee = two_departaments_data.drop_duplicates(subset="first_name", keep= "first")
    # its for can be deleted in the future, the iteration it wold be redundant 
    for index, row in only_employee.iterrows(): # iter to add employees with more than one departament
        departaments_in_one = list(two_departaments_data[two_departaments_data["first_name"] == row["first_name"]]["department"])

        employee = Employees(firstname=row["first_name"], lastname=row["last_name"])
        contact = Contacts(firstphonne=row["phone1"], secondaryphone=row["phone2"], email=row["email"])
        address = Addresses(zip_code=row["zip"], street=row["address"])
        
        state_addresses = States_addresses()
        city_addresses = Cities_addresses()
        employee_company = Employees_companies()


        if row["city"] not in city.keys() :
            city[row["city"]] = Cities(row["city"])
            db.session.add(city[row["city"]])
        if row["state"] not in state.keys() :
            state[row["state"]] = States(row["state"])
            db.session.add(state[row["state"]])
        if  row["company_name"] not in company.keys() :
            company[ row["company_name"]] = Companies(row["company_name"])
            db.session.add(company[row["company_name"]] )
        for dep in departaments_in_one:
            if  dep not in departaments.keys() :
                departaments[dep] = Departaments(dep)
                db.session.add(departaments[dep])
            employee.departaments.append(departaments[dep])
            
        employee.contact = contact
        employee_company.companies =   company[ row["company_name"]]
        employee.employees_companies = employee_company

        state_addresses.states =  state[row["state"]]
        address.states_addresses = state_addresses
            
        city_addresses.cities =  city[row["city"]]
        address.cities_addresses = city_addresses
        employee.address = address

        # adding information to database
        db.session.add(employee)
        db.session.add(contact)
        db.session.add(address)
        db.session.add(city_addresses)
        db.session.add(state_addresses)
        db.session.add(employee_company)
        db.session.commit()






        

        

    
    #print(sample_df)

# def add_data():
#     employ = Employees("Isay", "Castaneda")
#     contact = Contacts("3411002165", "3323749523", "icastaeda@gmail.com")
#     address = Addresses("5463", "Not", "21400")
#     street = Streets("Av mariano otero")
#     city = Cities("Guadalajara")
#     state = States("Jalisco")
#     company = Companies("Xaldigital")
#     dep1 = Departaments("Enginner")
#     dep2 = Departaments("Sales Force")
#     state_addresses = States_addresses()
#     city_addresses = Cities_addresses()
#     streets_addresses = Streets_addresses()
#     employee_company = Employees_companies()
  


#     employ.departaments.append(dep1)
#     employ.departaments.append(dep2)
#     employ.contact = contact
#     employee_company.companies = company
#     employ.employees_companies = employee_company

#     state_addresses.states = state
#     address.states_addresses = state_addresses
#     streets_addresses.street = street
#     address.street_addresses = streets_addresses
#     city_addresses.cities = city
#     address.cities_addresses = city_addresses
#     employ.address = address
    

#     db.session.add(employ)
#     db.session.add(contact)
#     db.session.add(address)
#     db.session.add(street)
#     db.session.add(streets_addresses)
#     db.session.add(city)
#     db.session.add(city_addresses)
#     db.session.add(state)
#     db.session.add(state_addresses)
#     db.session.add(company)
#     db.session.add(employee_company)
#     db.session.add(dep1)
#     db.session.add(dep2)

#     db.session.commit()

