select *
from alumnos join alumnos_niveles on alumnos.id = alumnos_niveles.alumno_id
			join niveles on alumnos_niveles.nivel_id = niveles.id
where niveles.nombre = 'Quinto' and niveles.seccion = 'A';

select *
from alumnos join alumnos_niveles on alumnos.id = alumnos_niveles.nivel_id
			join niveles on alumnos_niveles.nivel_id = niveles.id
where niveles.nombre='Tercero' and niveles.seccion='B';