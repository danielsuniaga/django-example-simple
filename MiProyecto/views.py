from django.http import HttpResponse

import datetime

from django.template import Template, Context

from django.template import loader

from django.shortcuts import render

def bienvenida(request): 

    return HttpResponse("Hola mundo")

def bienvenidaRojo(request): 

    return HttpResponse("<p style='color:red'>Hola mundo</p>")

def categoriaEdad(request, edad):

    if edad >= 18:

        if edad >= 60:

            categoria ="Tercera Edad"

        else:

            categoria = "Adultez"

    else:

        if edad < 10:

            categoria ="Infancia"

        else:

            categoria ="Adolescencia"

    resultado ="<h1>Categoria de la edad: %s</h1>" %categoria

    return HttpResponse(resultado)

def obtenerMomentoActual(request):

    #respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now())
    respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y"))
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre, edad):

    contenido="""
    <html>
    <body>
    <p> Nombre: %s / Edad: %s</p>
    </body> 
    </html>
    """ %(nombre,edad)

    return HttpResponse(contenido)

def miPrimeraPlantilla(request): 

    #Abrimos el documento html
    plantillaExterna = open("C:/Python37/Projects/Cursos/Django basico/MiProyecto/MiProyecto/plantillas/miPrimeraPlantilla.html")

    #asignamos ese documento a una plantilla
    template = Template(plantillaExterna.read())

    #Cerramos el documento
    plantillaExterna.close()

    #añadimos un contexto
    contexto = Context()

    #renderizamos el contexto
    documento = template.render(contexto)

    return HttpResponse(documento)

def plantillaParametros(request): 

    nombre ="Daniel Suniaga"

    fechaActual = datetime.datetime.now()

    lenguajes = ["Python","Ruby"]

    #Abrimos el documento html
    plantillaExterna = open("C:/Python37/Projects/Cursos/Django basico/MiProyecto/MiProyecto/plantillas/plantillaParametros.html")

    #asignamos ese documento a una plantilla
    template = Template(plantillaExterna.read())

    #Cerramos el documento
    plantillaExterna.close()

    #añadimos un contexto
    contexto = Context({"nombreusuario":nombre,"fechaActual":fechaActual,'lenguajes':lenguajes})

    #renderizamos el contexto
    documento = template.render(contexto)

    return HttpResponse(documento)

def plantillaCargador(request):

    nombre ="Daniel Suniaga"

    fechaActual = datetime.datetime.now()

    lenguajes = ["Python","Ruby"]
    #especificando la template que deseamos usar
    plantillaExterna = loader.get_template('plantillaParametros.html')

    #renderizar documento y enviamos.
    documento = plantillaExterna.render({"nombreusuario":nombre,"fechaActual":fechaActual,'lenguajes':lenguajes})

    return HttpResponse(documento)

def plantillaShortcut(request):

    nombre ="Daniel Suniaga"

    fechaActual = datetime.datetime.now()

    lenguajes = ["Python","Ruby"]

    return render(request, 'plantillaParametros.html', {"nombreusuario":nombre,"fechaActual":fechaActual,'lenguajes':lenguajes} )

def plantillaHija1(request):

    return render(request, "plantillaHija_1.html",{})

def plantillaHija2(request):

    return render(request, "plantillaHija_2.html",{})