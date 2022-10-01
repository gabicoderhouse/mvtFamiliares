from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

from mvtFamiliares.models import Familiar

def crear_familiar(request):    
    persona1 = Familiar(nombre='Ricardo', parentezco='Padre', edad=78,fecha_nacimiento = datetime(1934,7,11))
    persona2 = Familiar(nombre='Gerardo', parentezco='Pareja', edad=62,fecha_nacimiento = datetime(1960,1,1))
    persona3 = Familiar(nombre='Mauro', parentezco='Hijo', edad=27,fecha_nacimiento = datetime(1995,7,29))
    persona1.save()
    persona2.save()
    persona3.save()
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({})
    return HttpResponse(template_renderizado)

def ver_familiares(request):
    
    familiares = Familiar.objects.all()
    
    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares':familiares})
    
    return HttpResponse(template_renderizado)