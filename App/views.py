from django.shortcuts import render,redirect, get_object_or_404
from App.templates import *
from .models import *
from .forms import *
from django.core.paginator  import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def catalogo(request): 
    categoria_filtrada = request.GET.get('categoria')

    prods = productos.objects.all()

    if categoria_filtrada:
        prods = prods.filter(categoria=categoria_filtrada)


    total_productos = prods.count()  # Contar todos los productos antes de la paginación

    page = request.GET.get('page',1)

    productos_por_pagina = 15

    try:
        paginator = Paginator(prods, productos_por_pagina)
        prods = paginator.page(page)

    except EmptyPage:
        # Manejar la página vacía, por ejemplo, redirigir a la última página válida.
        prods = paginator.page(paginator.num_pages)

    except PageNotAnInteger:
        # Manejar el caso en que el número de página no es un entero.
        prods = paginator.page(1)
        
    except:
        raise Http404
    
    if 'borrar_filtros' in request.GET:
    # Redirigir a la misma vista sin los parámetros de filtro
        return redirect(to="catalogo")

    data = {
        'pro' : prods,
        'paginator' : paginator, 
        'total_productos': total_productos,   
        }
    
    return render(request, 'catalogo.html',data)

def contacto(request):
    data = { 'form' : contactoForm()}

    if request.method == 'POST':
        formulario = contactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data['form'] = formulario

    return render(request, 'contacto.html',data)

@login_required
def adm(request):
    return render(request,'admin.html')

def localrb(request):
    return render(request, 'localrb.html')

def nosotros(request):
    return render (request, 'nosotros.html')

@login_required
def ver_mensajes(request):
    msjs = Contacto.objects.all()
    data = {
            'msjs' : msjs
            }
    return render(request,'ver_mensajes.html',data)

@login_required
def mensaje(request,id):
    msj = get_object_or_404(Contacto, id=id)
    data = {'msj':msj}
    return render(request,'mensaje.html', data)

#==================================================================Productos=================================================================
#==================================================================Productos=================================================================
#==================================================================Productos=================================================================
#==================================================================Productos=================================================================
#==================================================================Productos=================================================================
#==================================================================Productos=================================================================

@login_required
def administrar_productos(request):
    prods = productos.objects.all()

    page = request.GET.get('page',1)

    productos_por_pagina = 10

    try:
        paginator = Paginator(prods, productos_por_pagina)
        prods = paginator.page(page)

    except EmptyPage:
        # Manejar la página vacía, por ejemplo, redirigir a la última página válida.
        prods = paginator.page(paginator.num_pages)

    except PageNotAnInteger:
        # Manejar el caso en que el número de página no es un entero.
        prods = paginator.page(1)
        
    except:
        raise Http404

    data = {
            'pro' : prods,
            'paginator' : paginator,    
            }
    return render (request,'Productos/adm_productos.html',data)

@login_required
def agregar_productos(request):
    data = {'form': Form_Agregar_Productos()}

    if request.method == 'POST':
        formulario = Form_Agregar_Productos(request.POST, request.FILES)
        if formulario.is_valid():
            # Obtener la categoría del campo oculto
            categoria_seleccionada = request.POST.get('categoria')
            # Asignar la categoría al campo en el formulario
            formulario.fields['categoria'].initial = categoria_seleccionada

            # Obtener la instancia del producto del formulario sin guardarlo aún
            producto = formulario.save(commit=False)

            # Asignar el valor 'True' al campo activo
            producto.activo = True

            # Guardar el formulario
            producto.save()

            return redirect(to="admP")
        else:
            data["form"] = formulario

    return render(request, 'Productos/agregar_productos.html', data)

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(productos, id=id)
    data = {'form': Form_Agregar_Productos(instance=producto)}
    
    # Agregar la categoría actual al contexto
    data['categoria_actual'] = producto.categoria

    if request.method == 'POST':
        formulario = Form_Agregar_Productos(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid:
            formulario.save()
            return redirect(to="admP")
        data ['form'] = formulario

    return render(request, 'Productos/editar_productos.html', data)

@login_required
def borrar_producto(request,id):
    producto = get_object_or_404(productos,id=id)
    producto.delete()
    return redirect(to="admP")

def ver_producto(request,id):
    producto = get_object_or_404(productos, id=id)
    data = {'producto':producto}
    return render (request,'Productos/ver_producto.html',data)

@login_required
def ver_producto_eliminar(request,id):
    producto = get_object_or_404(productos, id=id)
    data = {'producto':producto}
    return render (request,'Productos/ver_producto_eliminar.html',data)

@login_required
def editar_habilitado(request, id):
    producto = get_object_or_404(productos, id=id)

    if producto.activo:
        producto.activo = False
    else:
        producto.activo = True

    producto.save()

    # Devolver una respuesta JSON indicando el nuevo estado del producto
    return JsonResponse({'activo': producto.activo})

#==================================================================Servilletas=================================================================
#==================================================================Servilletas=================================================================
#==================================================================Servilletas=================================================================
#==================================================================Servilletas=================================================================
#==================================================================Servilletas=================================================================
#==================================================================Servilletas=================================================================

@login_required
def agregar_servilleta(request):
    data = {'form': Form_Agregar_Servilletas()}

    if request.method == 'POST':
        formulario = Form_Agregar_Servilletas(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admS")
        else:
            data["form"] = formulario

    return render(request, 'Servilletas/agregar_servilletas.html', data)

@login_required
def editar_servilleta(request,id):
    servilleta = get_object_or_404(Servilletas, id=id)
    data = {'form': Form_Agregar_Servilletas(instance=servilleta)}
    if request.method == 'POST':
        formulario = Form_Agregar_Servilletas(data=request.POST, files=request.FILES, instance=servilleta)
        if formulario.is_valid:
            formulario.save()
            return redirect(to="admS")
        data ['form'] = formulario
    return render (request,'Servilletas/editar_servilletas.html',data)

@login_required
def administrar_servilletas(request):
    servs = Servilletas.objects.all()

    page = request.GET.get('page',1)

    productos_por_pagina = 10

    try:
        paginator = Paginator(servs, productos_por_pagina)
        servs = paginator.page(page)

    except EmptyPage:
        # Manejar la página vacía, por ejemplo, redirigir a la última página válida.
        servs = paginator.page(paginator.num_pages) 

    except PageNotAnInteger:
        # Manejar el caso en que el número de página no es un entero.
        servs = paginator.page(1)
        
    except:
        raise Http404

    data = {
            'serv' : servs,
            'paginator' : paginator,    
            }
    return render (request,'Servilletas/adm_servilletas.html',data)

@login_required
def ver_servilleta_eliminar(request,id):
    servilleta = get_object_or_404(Servilletas, id=id)
    data = {'servilleta':servilleta}
    return render (request,'Servilletas/ver_servilleta_eliminar.html',data)

@login_required
def borrar_servilleta(request,id):
    servilleta = get_object_or_404(Servilletas,id=id)
    servilleta.delete()
    return redirect(to="admS")

def ver_servilleta(request,id):
    servilleta = get_object_or_404(Servilletas, id=id)
    data = {'servilleta':servilleta}
    return render (request,'Servilletas/ver_servilleta.html',data)

@login_required
def editar_habilitado_servilleta(request,id):
    servilleta = get_object_or_404(Servilletas, id=id)
    if servilleta.activo:
        servilleta.activo = False
    else:
        servilleta.activo = True
    servilleta.save()
    
    return JsonResponse({'activo': servilleta.activo})

def catalogo_servilleta(request): 

    serv = Servilletas.objects.all()

    total_productos = serv.count()  # Contar todos los productos antes de la paginación

    page = request.GET.get('page',1)

    productos_por_pagina = 15

    try:
        paginator = Paginator(serv, productos_por_pagina)
        serv = paginator.page(page)

    except EmptyPage:
        # Manejar la página vacía, por ejemplo, redirigir a la última página válida.
        serv = paginator.page(paginator.num_pages)

    except PageNotAnInteger:
        # Manejar el caso en que el número de página no es un entero.
        serv = paginator.page(1)
        
    except:
        raise Http404
    
    data = {
        'serv' : serv,
        'paginator' : paginator, 
        'total_productos': total_productos,   
        }
    
    return render(request, 'servilletas.html',data)

#==================================================================Login=================================================================
#==================================================================Login=================================================================
#==================================================================Login=================================================================
#==================================================================Login=================================================================
#==================================================================Login=================================================================
#==================================================================Login=================================================================
