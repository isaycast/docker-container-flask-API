from flask import Flask 

app = Flask(__name__)
# its necesary to pass the this path to env files have sensible information about data frame, could be future implementation
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@db/employees'

from app import views
from app import extensions