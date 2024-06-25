#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Conectar a la base de datos MySQL
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Crear un cursor para ejecutar las consultas
        cursor = db.cursor()

        # Ejecutar la consulta para seleccionar todos los estados ordenados por id
        cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

        # Recuperar todos los resultados de la consulta
        states = cursor.fetchall()

        # Imprimir los resultados
        for state in states:
            print(state)

        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()
        db.close()

    except MySQLdb.OperationalError as e:
        print(f"Error: {e}")
