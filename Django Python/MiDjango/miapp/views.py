from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# MVC modelo vista controlador
# MVT modelo template vista

layout = """
<h1>sitio web con Django ! Cristhian carrero
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">hola mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">pagina de pruenas</a>
    </li>
    <li>
        <a href="/contacto">contactos </a>
    </li>
</ul>
<hr/>
"""

def index(request):
    html ="""<h1>Inicio<//h1>
    <p>años hasta el 2050</p>
    <ul>
    """
    year = 2021
    while year <= 2050:
        if year%2 ==0:
            html += f"<li>{str(year)}</li>"
        year += 1
    return HttpResponse(layout+html)

def hola_Mundo(request):
    return HttpResponse(layout+"""
    <h1>hola mundo con Django!!</h1>
    <h2> Soy cristhian </h2>""")     

def pagina(request, redirigir=0):
    
    if redirigir == 1:
        return redirect('contacto', nombre="cristhian", apellidos="carrero")

    return HttpResponse(layout+"""
    <h1>Pagina de mi web</h1>
    <p>creado por cristhian</p>""")

def contacto(request, nombre = "", apellidos = ""): # parametros opcionales y tabn en la clase urls.py
    html = ""
    
    if nombre and apellidos:
        html += "El nombre completo es: "
        html += f"{nombre} {apellidos}"

    return HttpResponse(layout+f"""
    <h1>Pagina de contacto {nombre} {apellidos}</h1>
    """) 