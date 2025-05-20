from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador   # Importa las clases modelo para las tablas Club y Jugador
from configuracion import cadena_base_datos  # Importa la cadena de conexión a la base de datos

engine = create_engine(cadena_base_datos)  # Crea el motor para conectar con la base de datos
Session = sessionmaker(bind=engine)        # Crea una clase Session configurada para esa conexión
session = Session()                         # Instancia una sesión para manipular la base de datos

# Diccionario para almacenar clubes creados por nombre
clubes_creados = {}  # (No usado porque la parte que lee clubs está comentada)

# Parte comentada que leería y crea objetos Club desde el archivo datos_clubs.txt
with open("data/datos_clubs.txt", "r", encoding="utf-8") as archivo_clubes:
   for linea in archivo_clubes:
       nombre, deporte, fundacion = linea.strip().split(";")
       club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
       session.add(club)
       session.flush()  # Guarda temporalmente para asignar ID y poder usarlo luego
       clubes_creados[nombre] = club  # Guardar club en dict (útil para evitar consultas)

# Leer archivo datos_jugadores.txt para crear objetos Jugador
with open("data/datos_jugadores.txt", "r", encoding="utf-8") as archivo_jugadores:
    for linea in archivo_jugadores:
        # Cada línea tiene: nombre_club;posicion;dorsal;nombre_jugador
        nombre_club, posicion, dorsal, nombre = linea.strip().split(";")
        
        # Busca en la base de datos el club con ese nombre
        club = session.query(Club).filter_by(nombre=nombre_club).first()
        
        if club:
            # Si el club existe, crea el jugador asignado a ese club
            jugador = Jugador(nombre=nombre, dorsal=int(dorsal), posicion=posicion, club=club)
            session.add(jugador)  # Agrega jugador a la sesión
        else:
            # Si no encuentra el club, imprime un mensaje de error
            print(f"No se encontró el club '{nombre_club}' para el jugador '{nombre}'.")
            
session.commit()  # Confirma todas las transacciones para guardar en la base de datos

print("Datos cargados exitosamente.")  # Mensaje final
