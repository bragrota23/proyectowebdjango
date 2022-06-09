from django.db import models

# Create your models here.

class Reporte(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=600)
    imagen = models.ImageField(upload_to='reportes') 
    archivo_cotidiano = models.FileField(upload_to='archivos_cotidianos', null=True, blank=True)
    archivo_mensual = models.FileField(upload_to='archivos_mensuales', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='reporte'
        verbose_name_plural='reportes'
    
    def __str__(self):
        return self.titulo
