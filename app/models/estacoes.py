from sqlalchemy import Column, BigInteger, String, Numeric, Integer, CheckConstraint, DateTime

from sqlalchemy.sql.functions import current_timestamp

from app import db


class Estacoes(db.Model):

    __tablename__ = 'Estacoes'

    id_estacao = Column(BigInteger, primary_key=True)
    nome_estacao = Column(String(100), nullable=False)
    cod_regiao = Column(Numeric(2), CheckConstraint('cod_regiao >= 0'), nullable=False, server_default="0")
    uf = Column(String(2), nullable=False, server_default="0")
    codigo_wmo = Column(Numeric(10),CheckConstraint('cod_wmo >= 0'), nullable=False, server_default="0")
    latitude = Column(Numeric,CheckConstraint('latitude >= 0'), nullable=False, server_default="0")
    longitude = Column(Numeric,CheckConstraint('longitude >= 0'), nullable=False, server_default="0")
    altitude = Column(Numeric,CheckConstraint('altitude >= 0'), nullable=False, server_default="0")
    data_fundacao = Column(DateTime, server_default=current_timestamp())

    def __init__(self, id_estacao: str = "", nome_estacao: str = "", cod_regiao: float = 0, uf: str = "", codigo_wmo: float = 0, latitude: float = 0, longitude: float = 0, altitude: float = 0, data_fundacao: datetime = 00/00/0000) -> None:
        self.id_estacao = id_estacao
        self.nome_estacao = nome_estacao
        self.cod_regiao = cod_regiao
        self.uf = uf
        self.codigo_wmo = codigo_wmo
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.data_fundacao = data_fundacao

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Estacoes: {self.id_estacao}>'