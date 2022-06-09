from django.contrib import admin
from .models import Reporte
from import_export import resources 
from import_export.admin import ImportExportModelAdmin 


# Register your models here.

class ReporteResource(resources.ModelResource):
    class Meta:
        model = Reporte

class ReporteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields=('created','updated')
    resource_class=ReporteResource

admin.site.register(Reporte, ReporteAdmin)
