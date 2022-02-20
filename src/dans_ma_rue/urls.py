"""dans_ma_rue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



from dans_ma_rue import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # PAGE D'accueil
    path('', views.index, name = 'index'),
    path('q1/', include('q1.urls')),
    path('q2/', include('q2.urls')),
    path('q3/', include('q3.urls')),
]
 