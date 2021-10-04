/*
	* PRACTICA - MIA
	* VICTOR ALEJANDRO CUCHES DE LEON
	* 201807307
*/

-- CREADO Y BORRADO de base de datos propuesta en el modelo relacional

-- CREANDO TABLAS 
-- ***** Tablas independientes *****
-- Tabla Direccion
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

-- ELIMINANDO TABLAS 
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

