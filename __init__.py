from flask import Flask
app = Flask(__name__)
from .config import *
from .users import user
from .patient import patient

app.register_blueprint(user,url_prefix="")
app.register_blueprint(patient,url_prefix="")