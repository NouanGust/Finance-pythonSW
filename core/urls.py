from django.contrib import admin
from django.urls import path, include

#site.com/perfil
#site.com/perfil/home
#site.com/perfil/gerenciar

#Lista de urls do site path('nome_da_rota', ação)
#include('pasta.urls')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),

]



