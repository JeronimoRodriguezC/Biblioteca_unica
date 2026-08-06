import csv
import time
import mysql.connector
 
intentos = 10
for intento in range(intentos):
    try:
        conn = mysql.connector.connect(
            host="db",          
            port=3306,
            user="root",
            password="rootpassword",
            database="biblioteca_db"
        )
        print("Conectado a MySQL correctamente.")
        break

    except mysql.connector.Error as err:
        print(f"MySQL no está listo todavía... intento {intento + 1}/{intentos}")
        time.sleep(3)  # esperar 3 segundos antes de reintentar
else:
    raise Exception("No se pudo conectar a MySQL después de varios intentos.")

cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
    isbn varchar(20) PRIMARY KEY,
    titulo varchar(255),
    inicial_titulo char(1),
    autor varchar(500),
    editorial varchar(150),
    anio_de_publicacion INT,
    numero_de_paginas INT,
    idioma varchar(10),
    generos_palabras_clave varchar(400),
    dewey INT,
    cutter_sanborn varchar(8),
    rotulo_unica varchar(25),
    descripcion varchar(300)
    )
""")

conn.commit()
print("Tabla verificada/creada")


# Lee csv
sql = """
    INSERT INTO libros (
        isbn, titulo, inicial_titulo, autor, editorial, anio_de_publicacion, 
        numero_de_paginas, idioma, generos_palabras_clave, dewey, cutter_sanborn, rotulo_unica, 
        descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
with open("tabla_libros_biblioteca.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    valores = [tuple(row) for row in reader]

# pasa todo a la base de datos
cursor.executemany(sql, valores)
conn.commit()

print(f"Se insertaron {cursor.rowcount} registros.")

cursor.close()
conn.close()
        