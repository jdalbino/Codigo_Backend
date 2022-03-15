USE prueba;

INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
					('Estefani','73500746','DNI',true);
INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
					('Juan Diego','74501400','DNI',false);
INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
					('Juan Diego2','74501403','DNI',false),
                    ('Juan Diego2','74501402','DNI',false),
                    ('Juan Diego2','74501401','DNI',false);                    
SELECT id,nombre,documento FROM clientes;
SELECT * FROM clientes;

SELECT id,nombre,documento FROM clientes WHERE documento = '74501403' AND (nombre = 'Juan Diego' OR nombre = 'Juan Diego2');
SELECT id,nombre,documento FROM clientes WHERE documento LIKE '7%';

UPDATE clientes SET nombre = 'Juan Diegoo', documento = '123456' WHERE nombre='Juan Diego';

CREATE TABLE vacunas(
id INT PRIMARY KEY auto_increment,
nombre VARCHAR(100) UNIQUE NOT NULL,
estado BOOL DEFAULT TRUE,
fecha_vencimiento DATE,
procedencia ENUM('USA','CHINA','RUSIA','UK'),
lote VARCHAR(10)
);

CREATE TABLE vacunatorio(
id INT PRIMARY KEY auto_increment,
nombre VARCHAR(100) UNIQUE NOT NULL,
latitud FLOAT,
longitud FLOAT,
direccion VARCHAR(200),
horario_atencion VARCHAR(100),
vacuna_id INT,
FOREIGN KEY (vacuna_id) references vacunas (id)
);

SELECT * FROM clientes;

ALTER TABLE clientes DROP COLUMN dni;
ALTER TABLE vacunatorio DROP COLUMN latitud;
SELECT * FROM vacunatorio;
ALTER TABLE vacunatorio ADD COLUMN latitud FLOAT AFTER nombre;