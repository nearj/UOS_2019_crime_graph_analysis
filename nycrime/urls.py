from django.urls import path, include
from django.contrib import admin


from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('interface.urls')),
    path('clustering/', include('clustering.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)