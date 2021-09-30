#from flask import Flask

#app = Flask(__name__)

#@app.route('/')

#def hola():
#    return 'Hola Mundo 2.0 :D'

#@app.route('/uno')

#def hola2():
#    return 'Adios mundo 3.0 D:'


from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os


app = Flask(__name__)


#IMPLEMENTAR CORS PARA NO TENER ERRORES AL TRATAR ACCEDER AL SERVIDOR DESDE OTRO SERVER EN DIFERENTE LOCACIÓN
CORS(app)

DB_HOST = "localhost"
DB_NAME = "bd_practica" #bd_practica
DB_USER = "postgres" #postgres 
DB_PASS = "28800" #28800
try:
    con = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST)
    
    cur = con.cursor()
    
    print(con.status)
    
    #PANTALLA INICIAL
    @app.route("/")
    def hello():
      return "<h1 style='color:blue'>PANTALLA INICIAL DE PRACTICA</h1>"
    
    #Mostrar consulta #1

    #Mostrar consulta #2

    #Mostrar consulta #3

    #Mostrar consulta #4

    #Mostrar consulta #5

    #Mostrar consulta #6

    #Mostrar consulta #7

    #Mostrar consulta #8

    #Mostrar consulta #9

    #Mostrar consulta #10

    #Eliminar datos de la tabla temporal
    @app.route('/eliminarTemporal', methods=['GET'])
    def fetch_delete_temp_data():
        cureT = con.cursor()
        #cur.execute('SELECT * FROM temp_data')
        cureT.execute("""
            DELETE FROM temp_data;
        """)
        #rows = cur.fetchall()
        #print(rows)
        #HACER SIEMPRE COMMIT!!
        con.commit()
        print("listo")
        return "<h1 style='color:blue'>SE HA LIMPIADO LA TABLA TEMPORAL </h1>"

    #Elimina las tablas del modelo de datos

    #Carga masiva de datos a tabla temporal
    @app.route('/cargarTemporal', methods=['GET'])
    def fetch_all_movies():
        #cur.execute('SELECT * FROM temp_data')
        cur.execute("""
        copy temp_data from '/home/victorcuches/Descargas/BlockbusterData_PC.csv' USING delimiters ';' csv header encoding 'windows-1251'
        """)
        #rows = cur.fetchall()
        #print(rows)
        #HACER SIEMPRE COMMIT!!
        con.commit()
        print("listo")
        return "<h1 style='color:blue'>ARCHIVOS CARGADOS CORRECTAMENTE</h1>"

    #Crear tablas del modelo y cargarle los datos


    
    if __name__ == "__main__":
     app.run(host='0.0.0.0')        

except:
    print('Error')