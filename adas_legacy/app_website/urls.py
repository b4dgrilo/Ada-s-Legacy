from django.urls import path
from app_website import views


urlpatterns = [
    path('', views.index),
    path('cadastro/', views.cadastro),
    path('login/', views.login),
]







# urlpatterns = [
#      path('cadastro/', views.cadastro, name='cadastro'),
#      path('login/', views.login, name='login')
#     ]