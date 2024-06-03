from django.contrib import admin
from django.urls import include, path

from iamweb import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('security.urls')),
]


admin.site.site_title = "I Am Emerge Services"
admin.site.site_header = "I Am Emerge Pty Ltd"
admin.site.index_title = "I Am Emerge welcomes you!!!"


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)