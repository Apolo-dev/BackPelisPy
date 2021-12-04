
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('AppMovie.urls')),
    path('api/', include('AppUser.urls'))
]
