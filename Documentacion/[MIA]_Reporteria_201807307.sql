/*
	* PRACTICA - MIA 
	* VICTOR ALEJANDRO CUCHES DE LEON
	* 201807307
*/

-- ***** CONSULTAS *****

-- Consulta 1
-- Mostrar la cantidad de copias que existen en el inventario para la película “Sugar Wonka”.
SELECT COUNT (nombre_pelicula)FROM temp_data WHERE nombre_pelicula = 'SUGAR WONKA';

-- Consulta 2
/* Mostrar el nombre, apellido y pago total de todos los clientes que han
   rentado películas por lo menos 40 veces. */
   
SELECT 

-- Consulta 3
/* Mostrar el nombre y apellido (en una sola columna) de los actores que
   contienen la palabra “SON” en su apellido, ordenados por su primer nombre.*/
SELECT nombre_actor || ' ' || apellido_actor FROM actor WHERE apellido_actor LIKE '%son%';

-- Consulta 4





