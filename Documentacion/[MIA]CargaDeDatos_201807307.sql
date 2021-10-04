/*
	* PRACTICA - MIA
	* VICTOR ALEJANDRO CUCHES DE LEON
	* 201807307
*/

-- Carga y distribución de la información en la nueva base de datos
-- LLENANDO EL ER CON DATOS DE LA TABLA TEMPORAL
-- llenando tabla pais 
INSERT INTO pais(nombre_pais)
SELECT DISTINCT pais_cliente FROM temp_data WHERE pais_cliente <> '-'
UNION DISTINCT 
SELECT DISTINCT pais_empleado FROM temp_data WHERE pais_empleado <> '-'
UNION DISTINCT 
SELECT DISTINCT pais_tienda FROM temp_data WHERE pais_tienda <> '-';

SELECT * FROM pais;

-- llenando tabla ciudad 
INSERT INTO ciudad(nombre_ciudad)
SELECT DISTINCT ciudad_cliente FROM temp_data WHERE ciudad_cliente <> '-'
UNION DISTINCT 
SELECT DISTINCT ciudad_empleado FROM temp_data WHERE ciudad_empleado <> '-'
UNION DISTINCT 
SELECT DISTINCT ciudad_tienda FROM temp_data WHERE ciudad_tienda <> '-';

SELECT * FROM ciudad;

-- llenando tabla direccion
INSERT INTO direccion(direccion, codigo_postal)
SELECT DISTINCT direccion_cliente, codigo_postal_cliente FROM temp_data WHERE direccion_cliente <> '-' 
AND codigo_postal_cliente <> '-'
UNION DISTINCT 
SELECT DISTINCT direccion_empleado, codigo_postal_empleado FROM temp_data WHERE direccion_empleado <> '-'
AND codigo_postal_cliente <> '-'
UNION DISTINCT 
SELECT DISTINCT direccion_tienda, codigo_postal_tienda  FROM temp_data WHERE direccion_tienda <> '-'
AND codigo_postal_empleado <>'-';

SELECT * FROM direccion;

-- llenando tabla cliente
INSERT INTO cliente(nombre_cliente, apellido_cliente, correo_cliente, activo_cliente, fecha_registro, tienda_cliente)
SELECT DISTINCT nombre_cliente, apellido_cliente, correo_cliente, cliente_activo, fecha_creacion, tienda_preferida
FROM temp_data;

SELECT * FROM cliente;

-- llenando tabla empleado
INSERT INTO empleado(nombre_empleado, apellido_empleado, correo_empleado, activo_empleado, tienda_empleado, usuario_empleado, contrasena_empleado)
SELECT DISTINCT nombre_empleado, apellido_empleado, correo_empleado, empleado_activo, tienda_empleado, usuario_empleado, contrasena_empleado
FROM temp_data WHERE nombre_empleado <> '-';

SELECT * FROM empleado;

-- llenando tabla tienda
INSERT INTO tienda(nombre_tienda)
SELECT DISTINCT nombre_tienda FROM temp_data WHERE nombre_tienda <> '-';

SELECT * FROM tienda;

-- llenando tabla pelicula
INSERT INTO pelicula(titulo, descripcion, anio_lanzamiento, duracion, dias_renta, costo_renta, costo_dano)
SELECT DISTINCT nombre_pelicula, descripcion_pelicula, CAST(ano_lanzamiento AS INTEGER), CAST(duracion AS INTEGER), CAST(dias_renta AS INTEGER), CAST(costo_renta AS FLOAT), CAST(costo_por_ano AS FLOAT)
FROM temp_data
WHERE nombre_pelicula <>'-' AND descripcion_pelicula <>'-' AND ano_lanzamiento <>'-' AND duracion<>'-' AND dias_renta<>'-' AND costo_renta<>'-' AND costo_por_ano<>'-';

SELECT * FROM pelicula;

-- llenando tabla idioma 
INSERT INTO idioma(idioma) 
SELECT DISTINCT lenguaje_pelicula FROM temp_data WHERE lenguaje_pelicula <> '-';

SELECT * FROM idioma;

-- llenando tabla jefe_tienda
INSERT INTO jefe_tienda(nombre_jefe, apellido_jefe)
SELECT DISTINCT encargado_nombre_tienda, encargado_apellido_tienda FROM temp_data
WHERE encargado_nombre_tienda<>'-' AND encargado_apellido_tienda<>'-';

SELECT * FROM jefe_tienda;

-- llenando tabla clasificacion
INSERT INTO clasificacion(nombre_clasificacion)
SELECT DISTINCT clasificacion FROM temp_data WHERE clasificacion <>'-';

SELECT * FROM clasificacion;

-- llenando tabla categoria 
INSERT INTO categoria(tipo_categoria)
SELECT DISTINCT categoria_pelicula FROM temp_data WHERE categoria_pelicula<>'-';

SELECT * FROM categoria;

-- llenando tabla actores
INSERT INTO actor(nombre_actor, apellido_actor)
SELECT DISTINCT actor_nombre_pelicula, actor_apellido_pelicula FROM temp_data 
WHERE actor_nombre_pelicula<>'-' AND actor_apellido_pelicula<>'-';

SELECT * FROM actor;

-- llenando tabla renta_pelicula
INSERT INTO renta_pelicula(cantidad_pago, fecha_pago, fecha_renta, fecha_regreso)
SELECT DISTINCT CAST(monto_a_pagar AS FLOAT), fecha_pago, fecha_renta, fecha_retorno 
FROM temp_data;

SELECT * FROM renta_pelicula;