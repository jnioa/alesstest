from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('home.urls')),
    path('alesstest/', include('alesstest.urls')),
    path('hard/', include('hard.urls')),
    path('taiki/', include('taiki.urls')),
    path('taiki2/', include('taiki2.urls')),
    path('admin/', admin.site.urls),
]

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
