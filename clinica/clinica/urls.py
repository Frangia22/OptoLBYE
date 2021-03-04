from django.contrib import admin
from django.urls import path 
from django.conf.urls import include
#Agrego la app a la url y las sesiones
urlpatterns = [
    path('admin/', admin.site.urls),
    path('optometrialbye/', include('optometrialbye.urls')),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
