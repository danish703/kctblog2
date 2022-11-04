from django.contrib import admin
from django.urls import path
from .views import home, details, signup, signin, dashboard,signout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name="home"),
                  path('details/<int:id>', details, name='details'),
                  path('signup/', signup, name='signup'),
                  path('signin/', signin, name='signin'),
                  path('signout/', signout, name='signout'),
                  path('dashboard/', dashboard, name='dashboard'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
