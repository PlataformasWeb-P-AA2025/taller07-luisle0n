from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Obtener un listado de todos los registros 
# de la tabla Club, que tengan al menos 
# un jugador con el nombre que tenga incluida la cadena “Da”

# para la solución se hace uso del método 
# join aplicado a query

clubs = session.query(Club).join(Jugador).\
        filter(Jugador.nombre.like("%Da%")).all()
# print(clubs)
print("Consulta 1 ")
"""
Consulta 1 
Club: nombre=Barcelona deporte=Fútbol fundación=1920
"""
for e in clubs: 
    print(e)