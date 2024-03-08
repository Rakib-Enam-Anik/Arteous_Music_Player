from django.contrib import admin
from django.urls import path
from django.conf.urls import include

app_name = "first_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls')),
  
]
