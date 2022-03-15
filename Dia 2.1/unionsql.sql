use prueba;

select *
from vacunatorios inner join vacunas on vacunatorios.vacuna_id = vacunas.id;

select *
from vacunatorios left join vacunas on vacunatorios.vacuna_id = vacunas.id;

insert into vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) values
						('POST JOSE GALVEZ2',14.26598,32.2569,'AV. EL SOL 755','LUN-VIE 15:00 22:00',null,null);

select *
from vacunatorios left join vacunas on vacunatorios.vacuna_id = vacunas.id union
select *
from vacunatorios right join vacunas on vacunatorios.vacuna_id = vacunas.id;

select vacu.nombre, vac.nombre
from vacunatorios as vac join vacunas as vacu on vac.vacuna_id = vacu.id
where vacu.nombre = 'Pfizer';
--
select *
from vacunatorios join vacunas on vacunatorios.vacuna_id = vacunas.id
where vacunas.nombre='SINOPHARM' and horario_atencion LIKE '%LUN-VIE%';

select vacunas.nombre, latitud
from vacunatorios join vacunas on vacunatorios.vacuna_id = vacunas.id
where latitud > -5 and latitud <10;

select procedencia, vacunas.nombre
from vacunatorios right join vacunas on vacunatorios.vacuna_id = vacunas.id
where vacuna_id is null;