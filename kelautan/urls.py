from django.contrib import admin
from django.urls import path
from sik.views import halamanbaru, halamanlainnya

urlpatterns = [
    path('admin/', admin.site.urls),
    path('halamanbaru/', halamanbaru),
    path('halamanlainnya/', halamanlainnya),
]
