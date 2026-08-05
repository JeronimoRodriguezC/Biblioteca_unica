CREATE DATABASE IF NOT EXIST Biblioteca_db;

USE Biblioteca_db;

/* Creacion tabla par a almacenar datos*/
CREATE TABLE IF NOT EXIST  'libros' (
    isbn INT,
    titulo varchar(255),
    inicial_titulo char(1),
    autor varchar(100),
    editorial varchar(150),
    anio_de_publicacion INT,
    numero_de_paginas INT,
    idioma varchar(2),
    generos_palabras_clave varchar(400),
    dewey INT,
    cutter_sanborn varchar(8),
    rotulo_unica varchar(25),
    descripcion varchar(300)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
