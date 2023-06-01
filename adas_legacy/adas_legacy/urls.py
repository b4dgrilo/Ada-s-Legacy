
from django.contrib import admin
from django.urls import path
from app_website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #rota, view responsável, nome de referência
    # cadastro.com
    path('',views.cadastro,name='cadastro'),
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
