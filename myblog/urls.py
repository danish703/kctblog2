
from django.contrib import admin
from django.urls import path
from .views import home,details
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('details/<int:id>',details,name='details')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
