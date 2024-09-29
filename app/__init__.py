import os
from flask import Flask

app = Flask(__name__)

# app = Flask(__name__, template_folder=os.path.abspath('templates'))

from app import routes