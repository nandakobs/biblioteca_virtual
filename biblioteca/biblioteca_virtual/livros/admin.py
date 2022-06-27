from django.contrib import admin
from .models import Cadastro_livros
from django.contrib.admin.filters import SimpleListFilter

class CustomFilter(SimpleListFilter):
    title = "Filtro customizado"
    parameter_name = "filter"
    def lookups(self, request, model_admin):
        return(
            ("titulo", "Titulo"),
            ("autor", "Autor(a)"),
            ("editora", "Editora"),
        )
    def queryset(self, request, queryset):
        if self.value() == "titulo":
            queryset = queryset.order_by('titulo')
        elif self.value() == "autor":
            queryset = queryset.order_by('autor')
        elif self.value() == "editora":
            queryset = queryset.order_by('editora')
        return queryset

class Procura_livros(admin.ModelAdmin):
    search_fields = ['titulo']
    list_filter = ['titulo', CustomFilter]


admin.site.register(Cadastro_livros, Procura_livros)