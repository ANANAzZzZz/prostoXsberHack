from flask import Flask
from config import Config
from db.DBInterface import DBInterface

app = Flask(__name__)

db = DBInterface()


app.config.from_object(Config)

from app import routes