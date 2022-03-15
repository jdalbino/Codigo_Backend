-- Necesito una bd para almacenar los alumnos de mi colegio
-- mi colegio es solamente de primaria y solamente quiero almacenar
-- el alumno con su informacion que seria nombre, ape pat, ape mat, correo
-- numero de emergencia, y de cada seccion almacenar su nombre (A,B,C)
-- por si acaso el alumno puede cambiar pero por el momento no deseo las notas

-- alumnos (id, nombre, apellido paterno, apellido materno,correo, numero de emergencia, id_seccion, año, ubicacion)
-- secciones (id, nombre, id_alumno)
-- ubicaciones (id, nombre)
CREATE DATABASE colegios;
USE colegios;
CREATE TABLE IF NOT EXISTS alumnos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido_paterno VARCHAR(45),
    apellido_materno VARCHAR(45),
    correo VARCHAR(20) UNIQUE,
    numero_emergencia VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS niveles(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
    ubicacion varchar(45),
    seccion varchar(45) not null
);
CREATE TABLE IF NOT EXISTS alumnos_niveles(
	id INT PRIMARY KEY AUTO_INCREMENT,
    alumno_id int,
    nivel_id int,
    fecha_cursada year,
    FOREIGN KEY(alumno_id) REFERENCES alumnos(ID),
    FOREIGN KEY(nivel_id) REFERENCES niveles(ID)
)