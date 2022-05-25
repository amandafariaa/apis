# importa os codigos do instance/config
from instance import config

DEBUG = True

# APONTAMENTO DO BANCO DE DADOS
DATABASE = f'mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db}'

# OPÇOES DE CONECÇÃO DO BANCO DE DADOS
DATABASE_CONNECT_OPTIONS = { }

# NÃO FAÇO IDEIA
SQLALCHEMY_TRACK_MODIFICATIONS = False