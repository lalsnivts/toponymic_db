from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('toponymic_db/', include('toponymic_db.urls')),
    path('admin/', admin.site.urls),
]