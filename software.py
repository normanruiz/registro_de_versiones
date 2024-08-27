from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Software(Base):

    __tablename__ = 'softwares'

    cod_software = Column(Integer(), primary_key=True)
    software = Column(String(18), nullable=False, unique=True)
    fecha_creacion = Column(DateTime(), nullable=False)
    fecha_ultima_modificacion = Column(DateTime(), nullable=False, default=datetime.now())

