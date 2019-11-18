from django.db import models
from django.db.models import AutoField

#from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_conf import ConfUsuario
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_genr import GenrGeneral
#from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_mov import MovDetalleEmpleado


class MantPersona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    fecha_de_nacimiento = models.DateField(blank=False, null=False)
    estado = models.IntegerField(blank=False, null=False)
    foto = models.ImageField(blank=False, null=False)
    id_genr_genero = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="genero", db_column='id_genr_genero')
    id_genr_pais = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, db_column='id_genr_pais')
    id_genr_tipo_identificacion = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="identificacion", db_column='id_genr_tipo_identificacion')
    id_genr_estado_civil = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="estado_civil", db_column='id_genr_estado_civil')
    identificacion = models.CharField(unique=True, max_length=50, blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    correo = models.CharField(max_length=50, blank=False, null=False)
    fecha_ingreso = models.DateTimeField(blank=False, null=False)
    usuario_ing = models.CharField(max_length=60, blank=False, null=False)
    terminal_ing = models.CharField(max_length=60, blank=False, null=False)
    id_genr_tipo_sangre = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="tipo_de_sangre", db_column='id_genr_tipo_sangre')
    id_genr_etnia = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="etnia", db_column='id_genr_etnia')
    direccion = models.CharField(max_length=150, blank=False, null=False)
    id_genr_jornada = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="jornada", db_column='id_genr_jornada')
    id_genr_indigena = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="indigena", db_column='id_genr_indigena')
    id_genr_idioma_ancestral = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="acestral", db_column='id_genr_idioma_ancestral')
    celular = models.CharField(max_length=15, blank=False, null=False)
    lugar_nacimiento = models.CharField(max_length=45, blank=False, null=False)
    id_genr_provincia = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="provincia", db_column='id_genr_provincia')
    id_genr_ciudad = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="ciudad", db_column='id_genr_ciudad')
    id_genr_categoria_migratoria = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="categoria_migratoria", db_column='id_genr_categoria_migratoria')
    discapacidad = models.BooleanField(blank=False, null=False)
    discapacidad_renal = models.BooleanField(blank=False, null=False)
    discapacidad_neurologica = models.BooleanField(blank=False, null=False)
    enfermedad_alergica = models.BooleanField(blank=False, null=False)
    asma = models.BooleanField(blank=False, null=False)
    epilepsia = models.BooleanField(blank=False, null=False)
    enfermedad_congenita = models.BooleanField(blank=False, null=False)
    enfermedad_respiratoria = models.BooleanField(blank=False, null=False)
    atencion_psicologica = models.BooleanField(blank=False, null=False)
    bono_solidario = models.BooleanField(blank=False, null=False)
    mienbros_hogar = models.IntegerField(blank=False, null=False)
    id_genr_tipo_usuario = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="persona_tipo_usuario", db_column='id_genr_tipo_usuario')
    id_genr_estado_laboralp = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="estado_laboralp", db_column='id_genr_estado_laboralp')
    
    pnombres = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    papellidos = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    pidentificacion = models.CharField(max_length=15,unique=True, blank=False, null=True, default='no requerido')
    pdireccion = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    ptelefono = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    pvive_con_usted = models.BooleanField(blank=False, null=True, default=0)
    id_genr_estado_laboralm = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="estado_laboralm", db_column='id_genr_estado_laboralm', default=0)
    mnombres = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    mapellidos = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    mdireccion = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    mtelefono = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    midentificacion = models.CharField(max_length=15,unique=True, blank=False, null=True, default='no requerido')
    mvive_con_usted = models.BooleanField(blank=False, null=True, default=0)
    rnombres = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    rapellidos = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    rapellidos = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    rtelefono = models.CharField(max_length=45, blank=False, null=True, default='no requerido')
    id_genr_tipo_parentesco = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="tipo_parentesco", db_column='id_genr_tipo_parentesco', default=0)
    rvive_con_usted = models.BooleanField(blank=False, null=True, default=0)
    ridentificacion = models.CharField(unique=True, max_length=13, blank=False, null=True, default='no requerido')

    class Meta:
        verbose_name = 'Persona',
        verbose_name_plural = 'Personas',
        db_table = 'mant_persona'

    def __str__(self):
        return self.nombres

class MantRepresentante(models.Model):
    id_representante = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(MantPersona, on_delete=models.CASCADE, blank=False, null=False, db_column='id_persona')
    usuario_ing = models.CharField(max_length=45, blank=False, null=False)
    fecha_ingreso = models.DateTimeField(blank=False, null=False)
    terminal_ing = models.CharField(max_length=45, blank=False, null=False)
    id_genr_nivel_formacion = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, blank=False, null=False, db_column='id_genr_nivel_formacion')
    ingresos_totales = models.FloatField(blank=False, null=False)
    id_usuario = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name = 'Representante',
        verbose_name_plural = 'Representantes',
        db_table = 'mant_representante'

    def __str__(self):
        return self.usuario_ing, self.terminal_ing

class MantEstudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(MantPersona, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name="fk_estudiante_persona", db_column='id_persona')
    tipo_estudiante = models.CharField(max_length=45, blank=False, null=False)
    fecha_ingreso = models.DateTimeField(blank=False, null=False)
    usuario_ing = models.CharField(max_length=45, blank=False, null=False)
    terminal_ing = models.CharField(max_length=45, blank=False, null=False)

    class Meta:
        verbose_name = 'Estudiante',
        verbose_name_plural = 'Estudiantes',
        db_table = 'mant_estudiante'

    def __str__(self):
        return self.tipo_estudiante, self.usuario_ing

class MantAnioLectivo(models.Model):
    id_anio_lectivo = models.AutoField(primary_key=True)
    anio = models.IntegerField(blank=False, null=False)
    ciclo = models.IntegerField(blank=False, null=False)
    fecha_incio_ciclo = models.DateField(blank=False, null=False)
    fecha_fin_ciclo = models.DateField(blank=False, null=False)
    id_genr_estado = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, blank=False, null=False,
                                       related_name="fk_aniolectivo_estado", db_column='id_genr_estado')

    class Meta:
        verbose_name = 'Año lectivo',
        verbose_name_plural = 'Año lectivo',
        db_table = 'mant_anio_lectivo'

    def __str__(self):
        return self.ciclo, self.anio


class MantEmpleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(MantPersona, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name="fk_empleado_persona", db_column='id_persona')
    id_detalle_empleado = models.ForeignKey('MovDetalleEmpleado', on_delete=models.CASCADE, blank=False, null=False,
                                            related_name="fk_empleado_detalle", db_column='id_detalle_empleado')
    id_anio_lectivo = models.ForeignKey(MantAnioLectivo, on_delete=models.CASCADE, blank=False, null=False,
                                        related_name="fk_empleado_anio_lectivo", db_column='id_anio_lectivo')
    id_usuario = models.ForeignKey('ConfUsuario', on_delete=models.CASCADE, blank=False, null=False,
                                   related_name="fk_empleado_usuario", db_column='id_usuario')
    fecha_ingreso = models.DateTimeField(blank=False, null=False)
    usuario_ing = models.CharField(max_length=45, blank=False, null=False)
    terminal_ing = models.CharField(max_length=45, blank=False, null=False)

    class Meta:
        verbose_name = 'Empleado',
        verbose_name_plural = 'Empleados',
        db_table = 'mant_empleado'

    def __str__(self):
        return self.usuario_ing


