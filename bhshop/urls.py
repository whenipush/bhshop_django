
from django.contrib import admin
from django.urls import path
from bhshop import settings
from django.conf.urls.static import static


from home.views import index
from catalog.views import catalog_page



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('catalog/', catalog_page, name='catalog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

