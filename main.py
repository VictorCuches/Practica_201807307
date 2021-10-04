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
    @app.route('/consulta3', methods=['GET'])
    def fetch_consulta3():
        cur.execute('SELECT * FROM idioma')
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)

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
        #print("listo")
        return "<h1 style='color:blue'>SE HA LIMPIADO LA TABLA TEMPORAL </h1>"

    #Elimina las tablas del modelo de datos
    @app.route('/eliminarModelo', methods=['GET'])
    def fetch_eliminar_modelo():
        cureT = con.cursor()
        #cur.execute('SELECT * FROM temp_data')
        cureT.execute("""
            DROP TABLE if exists ciudad_pais;
            DROP TABLE if exists actor_pelicula;
            DROP TABLE if exists categoria_pelicula;
            DROP TABLE if exists traduccion;
            DROP TABLE if exists renta_pelicula;
            DROP TABLE if exists pelicula;
            DROP TABLE if exists inventario;
            DROP TABLE if exists jefe_tienda;
            DROP TABLE if exists empleado;
            DROP TABLE if exists tienda;
            DROP TABLE if exists ciudad;
            DROP TABLE if exists cliente;
            DROP TABLE if exists Idioma;
            DROP TABLE if exists Actor;
            DROP TABLE if exists Categoria;
            DROP TABLE if exists Clasificacion;
            DROP TABLE if exists Pais;
            DROP TABLE if exists Direccion;
        """)
        #rows = cur.fetchall()
        #print(rows)
        #HACER SIEMPRE COMMIT!!
        con.commit()
        #print("listo")
        return "<h1 style='color:blue'>SSE HAN ELIMINADO LAS TABLAS DEL MODELO</h1>"

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
        #print("listo")
        return "<h1 style='color:blue'>ARCHIVOS CARGADOS CORRECTAMENTE</h1>"

    #Crear tablas del modelo y cargarle los datos
    @app.route('/cargarModelo', methods=['GET'])
    def fetch_cargar_modelo():
        #cur.execute('SELECT * FROM temp_data')
        cur.execute("""

        CREATE TABLE Direccion(
            id_Direccion serial PRIMARY KEY,
            direccion varchar(50),
            codigo_postal varchar(30)
        );

        -- Tabla Pais
        CREATE TABLE Pais(
            id_Pais serial PRIMARY KEY,
            nombre_pais varchar(40)
        );

        -- Tabla Clasificacion 
        CREATE TABLE Clasificacion (
            id_Clasificacion serial PRIMARY KEY,
            nombre_clasificacion varchar(30)
        );

        -- Tabla Categoria
        CREATE TABLE Categoria(
            id_Categoria serial PRIMARY KEY,
            tipo_categoria varchar(30)
        );

        -- Tabla Actor 
        CREATE TABLE Actor(
            id_Actor serial PRIMARY KEY,
            nombre_Actor varchar(30),
            apellido_Actor varchar(30)
        );

        -- Tabla Idioma
        CREATE TABLE Idioma(
            id_Idioma serial PRIMARY KEY,
            idioma varchar(30)
        );

        -- ***** Tablas dependientes *****
        CREATE TABLE cliente(
            id_Cliente serial PRIMARY KEY,
            nombre_Cliente varchar(30),
            apellido_Cliente varchar(30),
            correo_Cliente varchar(40),
            activo_Cliente varchar(10),
            fecha_registro varchar(30),
            tienda_Cliente varchar(20),
            id_Direccion2 integer,
            FOREIGN KEY  (id_Direccion2) REFERENCES Direccion(id_Direccion)
        );

        CREATE TABLE ciudad(
            id_Ciudad serial PRIMARY KEY,
            nombre_Ciudad varchar(30),
            id_Direccion3 integer,
            FOREIGN KEY  (id_Direccion3) REFERENCES Direccion(id_Direccion)
        );

        CREATE TABLE tienda(
            id_Tienda serial PRIMARY KEY,
            nombre_Tienda varchar(30),
            id_Direccion4 integer,
            FOREIGN KEY (id_Direccion4) REFERENCES Direccion(id_Direccion)
        );

        CREATE TABLE Empleado(
            id_Empleado serial PRIMARY KEY,
            nombre_Empleado varchar(30),
            apellido_Empleado varchar(30),
            correo_Empleado varchar(40),
            activo_Empleado varchar(10),
            tienda_Empleado varchar(20),
            usuario_Empleado varchar(30),
            contrasena_Empleado varchar(50),
            id_Tienda2 integer, 
            id_Direccion5 integer,
            FOREIGN KEY (id_Tienda2) REFERENCES Tienda(id_Tienda),
            FOREIGN KEY (id_Direccion5) REFERENCES Direccion(id_Direccion)
        );

        CREATE TABLE jefe_tienda(
            id_Jefe serial PRIMARY KEY,
            nombre_Jefe varchar(30),
            apellido_Jefe varchar(30),
            id_Tienda3 integer, 
            FOREIGN KEY (id_Tienda3) REFERENCES Tienda(id_Tienda)
        );

        CREATE TABLE inventario(
            id_Inventario serial PRIMARY KEY,
            id_Tienda4 integer,
            FOREIGN KEY (id_Tienda4) REFERENCES Tienda(id_Tienda)
        );

        CREATE TABLE pelicula(
            id_Pelicula serial PRIMARY KEY,
            titulo varchar(40),
            descripcion varchar(200),
            anio_lanzamiento integer, 
            duracion integer,
            dias_renta integer,
            costo_renta float,
            costo_dano float,
            id_Clasificacion2 integer,
            id_Idioma2 integer,
            id_Inventario2 integer,
            FOREIGN KEY (id_Clasificacion2) REFERENCES Clasificacion(id_Clasificacion),
            FOREIGN KEY (id_Idioma2) REFERENCES Idioma(id_Idioma),
            FOREIGN KEY (id_Inventario2) REFERENCES inventario(id_Inventario)
        );

        CREATE TABLE renta_pelicula(
            id_Renta serial PRIMARY KEY,
            cantidad_pago float,
            fecha_pago varchar(30),
            fecha_renta varchar(30),
            fecha_regreso varchar(30),
            id_Empleado2 integer,
            id_Pelicula2 integer, 
            id_Tienda5 integer, 
            FOREIGN KEY (id_Empleado2) REFERENCES empleado(id_Empleado),
            FOREIGN KEY (id_Pelicula2) REFERENCES pelicula(id_Pelicula),
            FOREIGN KEY (id_Tienda5) REFERENCES tienda(id_Tienda)	
        );

        CREATE TABLE traduccion(
            id_Traduccion serial PRIMARY KEY,
            traduccion varchar(50),
            id_Idioma3 integer,
            FOREIGN KEY (id_Idioma3) REFERENCES idioma(id_Idioma)
        );

        -- ***** MASTER-DETALLE *****
        CREATE TABLE categoria_pelicula(
            id_Pelicula3 integer,
            id_Categoria2 integer, 
            FOREIGN KEY (id_Pelicula3) REFERENCES pelicula(id_Pelicula),
            FOREIGN KEY (id_Categoria2) REFERENCES categoria(id_Categoria)
        );

        CREATE TABLE actor_pelicula(
            id_Actor2 integer,
            id_Pelicula4 integer,
            FOREIGN KEY (id_Actor2) REFERENCES actor(id_Actor),
            FOREIGN KEY (id_Pelicula4) REFERENCES pelicula(id_Pelicula)	
        );

        CREATE TABLE ciudad_pais(
            id_Pais2 integer,
            id_Ciudad2 integer,
            FOREIGN KEY (id_Pais2) REFERENCES pais(id_Pais),
            FOREIGN KEY (id_Ciudad2) REFERENCES ciudad(id_Ciudad)
        );
     
        INSERT INTO pais(nombre_pais)
        SELECT DISTINCT pais_cliente FROM temp_data WHERE pais_cliente <> '-'
        UNION DISTINCT 
        SELECT DISTINCT pais_empleado FROM temp_data WHERE pais_empleado <> '-'
        UNION DISTINCT 
        SELECT DISTINCT pais_tienda FROM temp_data WHERE pais_tienda <> '-';

  

        INSERT INTO ciudad(nombre_ciudad)
        SELECT DISTINCT ciudad_cliente FROM temp_data WHERE ciudad_cliente <> '-'
        UNION DISTINCT 
        SELECT DISTINCT ciudad_empleado FROM temp_data WHERE ciudad_empleado <> '-'
        UNION DISTINCT 
        SELECT DISTINCT ciudad_tienda FROM temp_data WHERE ciudad_tienda <> '-';

       

        INSERT INTO direccion(direccion, codigo_postal)
        SELECT DISTINCT direccion_cliente, codigo_postal_cliente FROM temp_data WHERE direccion_cliente <> '-' 
        AND codigo_postal_cliente <> '-'
        UNION DISTINCT 
        SELECT DISTINCT direccion_empleado, codigo_postal_empleado FROM temp_data WHERE direccion_empleado <> '-'
        AND codigo_postal_cliente <> '-'
        UNION DISTINCT 
        SELECT DISTINCT direccion_tienda, codigo_postal_tienda  FROM temp_data WHERE direccion_tienda <> '-'
        AND codigo_postal_empleado <>'-';

     

      
        INSERT INTO cliente(nombre_cliente, apellido_cliente, correo_cliente, activo_cliente, fecha_registro, tienda_cliente)
        SELECT DISTINCT nombre_cliente, apellido_cliente, correo_cliente, cliente_activo, fecha_creacion, tienda_preferida
        FROM temp_data;

   


        INSERT INTO empleado(nombre_empleado, apellido_empleado, correo_empleado, activo_empleado, tienda_empleado, usuario_empleado, contrasena_empleado)
        SELECT DISTINCT nombre_empleado, apellido_empleado, correo_empleado, empleado_activo, tienda_empleado, usuario_empleado, contrasena_empleado
        FROM temp_data WHERE nombre_empleado <> '-';

     

    
        INSERT INTO tienda(nombre_tienda)
        SELECT DISTINCT nombre_tienda FROM temp_data WHERE nombre_tienda <> '-';

 
        INSERT INTO pelicula(titulo, descripcion, anio_lanzamiento, duracion, dias_renta, costo_renta, costo_dano)
        SELECT DISTINCT nombre_pelicula, descripcion_pelicula, CAST(ano_lanzamiento AS INTEGER), CAST(duracion AS INTEGER), CAST(dias_renta AS INTEGER), CAST(costo_renta AS FLOAT), CAST(costo_por_ano AS FLOAT)
        FROM temp_data
        WHERE nombre_pelicula <>'-' AND descripcion_pelicula <>'-' AND ano_lanzamiento <>'-' AND duracion<>'-' AND dias_renta<>'-' AND costo_renta<>'-' AND costo_por_ano<>'-';


        INSERT INTO idioma(idioma) 
        SELECT DISTINCT lenguaje_pelicula FROM temp_data WHERE lenguaje_pelicula <> '-';

  

  
        INSERT INTO jefe_tienda(nombre_jefe, apellido_jefe)
        SELECT DISTINCT encargado_nombre_tienda, encargado_apellido_tienda FROM temp_data
        WHERE encargado_nombre_tienda<>'-' AND encargado_apellido_tienda<>'-';


        INSERT INTO clasificacion(nombre_clasificacion)
        SELECT DISTINCT clasificacion FROM temp_data WHERE clasificacion <>'-';


        INSERT INTO categoria(tipo_categoria)
        SELECT DISTINCT categoria_pelicula FROM temp_data WHERE categoria_pelicula<>'-';


        INSERT INTO actor(nombre_actor, apellido_actor)
        SELECT DISTINCT actor_nombre_pelicula, actor_apellido_pelicula FROM temp_data 
        WHERE actor_nombre_pelicula<>'-' AND actor_apellido_pelicula<>'-';


        INSERT INTO renta_pelicula(cantidad_pago, fecha_pago, fecha_renta, fecha_regreso)
        SELECT DISTINCT CAST(monto_a_pagar AS FLOAT), fecha_pago, fecha_renta, fecha_retorno 
        FROM temp_data;



        """)
        #rows = cur.fetchall()
        #print(rows)
        #HACER SIEMPRE COMMIT!!
        con.commit()
        #print("listo")
        return "<h1 style='color:blue'>TABLAS CREADAS Y DATOS CARGADOS</h1>"  



    
    if __name__ == "__main__":
     app.run(host='0.0.0.0')        

except:
    print('Error')