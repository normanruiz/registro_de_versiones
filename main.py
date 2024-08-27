# importar todo lo nesesario
import json
from software import Software
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cargar archivo de datos
datos_software = {}
with open("lote_software.json", "r", encoding="utf8") as file:
    datos_software = json.load(file)
print(datos_software)

# Cargar archivo de configuracion
datos_conexion = {}
with open("configuracion.json", "r", encoding="utf8") as file:
    datos_conexion = json.load(file)
print(datos_conexion)

#
engine = create_engine(f"mysql+pymysql://{datos_conexion['conexion']['user']}:{datos_conexion['conexion']['password']}@{datos_conexion['conexion']['host']}/{datos_conexion['conexion']['database']}", connect_args=dict(host=f"{datos_conexion['conexion']['host']}", port=int(f"{int(datos_conexion['conexion']['port'])}")))
Session = sessionmaker(bind=engine)
session = Session()

# Cargar el software
for softwaredata in datos_software["software"]["crear"]:
    softwareaux = Software(software=softwaredata["software"], fecha_creacion=datetime.now())
    session.add(softwareaux)
    session.commit()

# Cargar la plantilla