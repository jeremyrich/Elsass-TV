
from django.contrib import admin
from django.urls import path, include

import Elsasstv.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('movies/', include('movies.urls')),

]
