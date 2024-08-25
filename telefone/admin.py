from django.contrib import admin
from .models import Telefone, SeuModelo
from .models import TelefoneConsulta

@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nome', 'descricao')
    search_fields = ('numero', 'nome')
    list_filter = ('nome',)

@admin.register(SeuModelo)
class SeuModeloAdmin(admin.ModelAdmin):
    list_display = ('campo1', 'campo2', 'campo3')
    search_fields = ('campo1',)
    list_filter = ('campo2',)

@admin.register(TelefoneConsulta)
class TelefoneConsultaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'numero', 'data_consulta')
    search_fields = ('usuario__username', 'numero')

    def has_module_permission(self, request):
        return request.user.is_superuser