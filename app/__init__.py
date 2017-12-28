from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# Create a db instance
db = SQLAlchemy(app)

# Create a db migration instance
db_migrate = Migrate(app, db)

from app import routes, models
