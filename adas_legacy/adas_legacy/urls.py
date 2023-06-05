#import para carregar arquivos estaticos
from django.conf import settings
from django.conf.urls.static import static




from django.contrib import admin
from django.urls import path
from app_website.views import index, cadastro, login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('cadastro/', cadastro),
    path('login/', login),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


