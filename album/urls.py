
from django.contrib import admin
from django.urls import conf, path,include


#ami for static folder
from django.conf.urls.static import static
from django.conf import settings




#_____CHANGE ADMIN PANEL_____
admin.site.site_header = 'A awesome Site'
admin.site.site_title = 'Album'
admin.site.index_title = 'Some album'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('bootstrap.urls',namespace='bootstrap')),
    path('carusel/',include('carusel.urls',namespace='carusel')),
    path('dalbum/',include('dalbum.urls',namespace='dalbum')),
   
]


#ami for static foder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                   document_root = settings.MEDIA_ROOT)