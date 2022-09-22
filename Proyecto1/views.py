from django.http import HttpResponse

def saludo (reques): #primera vista 

    return HttpResponse('Primera pagina con django')

def despedida (reques): 
    return HttpResponse('Hasta luego')