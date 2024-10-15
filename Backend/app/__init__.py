import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Povolíme CORS pro všechny routy
CORS(app)
#CORS (Cross-Origin Resource Sharing) je bezpečnostní mechanismus implementovaný v prohlížečích, 
#který kontroluje, zda je dovoleno, aby webová stránka na jednom serveru (doméně) prováděla požadavky na jiný server (doménu).


from app import routes