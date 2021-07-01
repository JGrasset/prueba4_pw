from django.urls import path
from .views import home, registro, mk_libro, mod_libro, delete_libro, reg_user

urlpatterns=[
    path('', home, name="home"),
    path('registro', registro, name="registro.html"),
    path('mk-libro', mk_libro, name="mk_libro"),
    path('mod_libro/<id>', mod_libro, name="mod_libro"),
    path('delete_libro/<id>', delete_libro, name="dl_libro"),
    path('registro_usuario', reg_user, name="reg_user"),
]