from django.contrib import admin

admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'AProf '
admin.site.site_title = 'Aperfeiçoamento Profissional'

from core.models import Curso
from core.models import Turma
from core.models import Professor


class professorInline(admin.TabularInline):
    model = Professor
    max_num = 1


class turmaAdmin(admin.ModelAdmin):
    inlines = [
        professorInline,
    ]


class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'carga_horaria'
    )


admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma, turmaAdmin)
admin.site.register(Professor)
