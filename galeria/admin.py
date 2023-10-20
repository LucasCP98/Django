from django.contrib import admin
from galeria.models import Fotografia


@admin.register(Fotografia)
class CargoAdmin(admin.ModelAdmin):
    # nomes das tabelas.
    list_display = ('id', 'nome', 'legenda', 'categoria', 'descricao', 'foto', 'publicada', 'data_fotografia')
    # links.
    list_display_links = ('id', 'nome')
    # Busca pelo nome.
    search_fields = ('nome',)
    # Filtro pela tupla feita em models.
    list_filter = ('categoria',)
    # Quantidade de pagina.
    list_per_page = 10
    # ...
    list_editable = ('publicada',)
    # Na documentação dá para adiconar mais coisas https://docs.djangoproject.com/en/4.2/ref/contrib/admin/.





