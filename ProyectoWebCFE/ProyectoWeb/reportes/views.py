from django.shortcuts import render
from reportes.models import Reporte

# Create your views here.

def reportes(request):
    reportes=Reporte.objects.all()
    return render(request, "reportes/reportes.html",{"reportes": reportes}) 