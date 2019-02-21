
from django.contrib import admin
from django.urls import path, include

import Elsasstv.views as views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('movies/', include('movies.urls')),
    path('accounts/', include('accounts.urls')),
    path('search/', include('search.urls')),
        
]
