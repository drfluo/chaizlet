from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'jesuisunchocolatetcestcool'
from app import routes

