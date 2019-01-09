from django.db import models
from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATE_FORMAT = "d M Y"
pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"


class Curso(models.Model):
    nome = models.CharField('Nome do Curso', max_length=100)
    carga_horaria = models.IntegerField('Carga Horaria')
    ementa = models.CharField('Ementa', max_length=50)
    valor = models.FloatField('Valor')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Cursos'
        verbose_name = 'Curso'


class Turma(models.Model):
    data_inicio = models.DateField()
    data_termino = models.DateField('Data de Termino')
    hora_inicio = models.TimeField('Horario de Inicio')
    hora_termino = models.TimeField('Horario de Termino')

    class Meta:
        verbose_name_plural = 'Turmas'
        verbose_name = 'Turma'


class Professor(models.Model):
    nome = models.CharField('Nome', max_length=50)
    telefone = models.CharField('Telefoene', max_length=15)
    valor_hora_aula = models.FloatField()
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
