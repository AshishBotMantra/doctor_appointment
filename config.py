from extension import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONN'] = False
app.config['SECRET_KEY'] = 'thesecretkey'

db = SQLAlchemy(app)
ma = Marshmallow(app)