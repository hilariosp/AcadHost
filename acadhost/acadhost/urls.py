from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('avaliacao/', include('avaliacao.urls')),
    path('projeto/', include('projeto.urls')), 
    # path('usuario/', include('usuarios.urls')),
    # path ('account/', include('django.contrib.auth.urls')),          
]