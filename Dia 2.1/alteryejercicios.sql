USE prueba;

INSERT INTO vacunas (nombre, estado, fecha_vencimiento, procedencia, lote) VALUES
                    ('PFIZER', true, '2022-08-16', 'USA', '123jkl'),
                    ('SINOPHARM', true, '2022-10-10', 'CHINA', 'vxcvxc'),
                    ('MODERNA', true, '2022-09-14', 'USA', 'zxczxc'),
                    ('SPUTNIK', false, '2022-10-04', 'RUSIA', 'ghjkhjfg');
INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
                        ('CAMINO REAL', 14.121, -21.121, 'AV GIRASOL 115', 'LUN-VIE 07:00 - 15:00', null, 1),
                        ('HOSP. GNRAL.', 17.521, 11.1891, 'AV CIRCUNVALACION S/N', 'LUN-VIE 07:00 - 15:00', 'hospital.jpg', 2),
                        ('POSTA CERRO AZUL', 11.258, 67.447, 'AAHH LOS QUERUBINES LOTE 3 MZ J', 'LUN-SAB 07:00 - 15:00', 'foto01.png', 1),
                        ('ESTADIO LOS PALITOS', 24.121, -21.121, 'CALLE ESPINOSA 1115', 'LUN-MIE-VIE 07:00 - 15:00', 'est0001.jpg', 3),
                        ('PLAZA DEL AMOR', 4.116, -21.121, 'AV DE LOS HEROES ANONIMOS S/N', 'LUN-VIE 07:00 - 15:00', null, 1);
                        
SELECT * FROM vacunatorios;
alter table vacunatorio add column foto text after horario_atencion;
alter table vacunatorio rename to vacunatorios;
SELECT * FROM vacunatorios;
SELECT * FROM vacunas;
-- 1. Mostrar los nombres de las vacunas
select id,nombre from vacunas;
-- 2. Mostrar las vacunas que sean de procedencia USA
select id,nombre,procedencia from vacunas where procedencia = 'USA';
-- 3. Mostrar las vacunas que NO sean de procedencia USA
select id,nombre,procedencia from vacunas where procedencia != 'USA';
-- 4. Mostrar las vacunas que en su lote tengan los digitos 'xc'
select id,nombre,lote from vacunas where lote like '%xc%';
-- 5. Mostrar todos los vacunatorios que tengan horario de atencion los dias miercoles
select id,nombre, horario_atencion from vacunatorios where horario_atencion like '%LUN-VIE%' or horario_atencion like '%LUN-MIE-VIE%' or horario_atencion like '%LUN-SAB%';
-- 6. Mostrar todos los vacunatorios que tengan la vacuna_id 1 pero que tengan foto
select id,nombre from vacunatorios where vacuna_id = 1 and foto != 'null';