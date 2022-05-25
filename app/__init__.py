from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)


#CORS(app)

from app.models import estacoes

db.create_all()

# importar as classes controladoras
from app.controllers.estacoes_controller import EstacoesController
app.register_blueprint(EstacoesController.estacoes_controller, url_prefix="/api/v1/")

