from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('catalogo/', catalogo, name="catalogo"),
    path('contacto/', contacto, name="contacto"),
    path('adm/', adm, name="adm"),
    path('adm_productos', administrar_productos, name="admP"),
    path('agregar_productos', agregar_productos, name="addP"),
    path('editar_producto/<id>', editar_producto, name="editP"),
    path('ver_producto/<id>', ver_producto, name="verP"),
    path('eliminar_producto/<id>', ver_producto_eliminar, name="verPE"),
    path('borrar_producto/<id>',borrar_producto,name="borrarP"),
    path('habilitar_producto/<id>',editar_habilitado, name="habilitarP"),



    path('local_rb/',localrb, name="localrb"),
    path('nosotros/', nosotros, name="nosotros"),
    path('mensajes/',ver_mensajes, name="msjs"),
    path('msj/<id>',mensaje, name="msj"),

    ##============================================================================
    ##==================================Servilletas==========================================
    ##============================================================================
    path('agregar_servilletas/', agregar_servilleta, name="addS"),
    path('editar_servilletas/<id>', editar_servilleta, name="editS"),
    path('adm_servilletas', administrar_servilletas, name="admS"),
    path('eliminar_servilleta/<id>', ver_servilleta_eliminar, name="verSE"),
    path('borrar_servilleta/<id>',borrar_servilleta,name="borrarS"),
    path('ver_servilletas/<id>', ver_servilleta, name="verS"),
    path('habilitar_servilletas/<id>',editar_habilitado_servilleta, name="habilitarS"),
    path('servilletas/', catalogo_servilleta, name="catalogoS"),


]
