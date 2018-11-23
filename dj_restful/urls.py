from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    url('main/', include('main.urls')),
]
