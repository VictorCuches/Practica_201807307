/*
	* PRACTICA - MIA
	* VICTOR ALEJANDRO CUCHES DE LEON
	* 201807307
*/

-- TABLA TEMPORAL 
-- CARGA MASIVA de archivo csv
copy temp_data from '/home/victorcuches/Descargas/BlockbusterData_PC.csv' USING delimiters ';' csv header encoding 'windows-1251';

-- MOSTRAR registros guardados en tabla temporal
SELECT * FROM temp_data;

-- ELIMINAR registros guardados en tabla temporal
DELETE FROM temp_data;

-- CREACION de la tabla temporal
CREATE TABLE temp_data(
	nombre_cliente varchar(40),
	apellido_cliente varchar(40),
	correo_cliente varchar(40),
	cliente_activo varchar(40),
	fecha_creacion varchar(40),
	tienda_preferida varchar(40),
	direccion_cliente varchar(40),
	codigo_postal_cliente varchar(40),
	ciudad_cliente varchar(40),
	pais_cliente varchar(40),
	fecha_renta varchar(40),
	fecha_retorno varchar(40),
	monto_a_pagar varchar(40),
	fecha_pago varchar(40),
	nombre_empleado varchar(40),
	apellido_empleado varchar(40),
	correo_empleado varchar(40),
	empleado_activo varchar(40),
	tienda_empleado varchar(40),
	usuario_empleado varchar(40),
	contrasena_empleado varchar(40),
	direccion_empleado varchar(40),
	codigo_postal_empleado varchar(40),
	ciudad_empleado varchar(40),
	pais_empleado varchar(40),
	nombre_tienda varchar(40),
	encargado_nombre_tienda varchar(40),
	encargado_apellido_tienda varchar(40),
	direccion_tienda varchar(40),
	codigo_postal_tienda varchar(40),
	ciudad_tienda varchar(40),
	pais_tienda varchar(40),
	tienda_pelicula varchar(40),
	nombre_pelicula varchar(40),
	descripcion_pelicula varchar(40),
	ano_lanzamiento varchar(40),
	dias_renta varchar(40),
	costo_renta varchar(40),
	duracion varchar(40),
	costo_por_ano varchar(40),
	clasificacion varchar(40),
	lenguaje_pelicula varchar(40),
	categoria_pelicula varchar(40),
	actor_nombre_pelicula varchar(40),
	actor_apellido_pelicula varchar(40)
);
