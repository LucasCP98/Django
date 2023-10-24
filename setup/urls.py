from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('galeria.urls')),
                  path('', include('usuarios.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# a linha a cima + Static(..., serve para referenciar o media, static etc que estão no arquivo
# settings do setup.
