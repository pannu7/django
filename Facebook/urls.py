from django.contrib import admin
from django.urls import path,include
from Facebook.views import home
urlpatterns = [
    path('', home),
    # path('admin/', admin.site.urls),
]
