"""blog_son URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog.views import politic, sport, tech, home, post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('posts/<int:post_pk>', post),
    path('politic/', politic, name='politic'),
    path('sport/', sport, name='sport'),
    path('tech/', tech, name='tech')
]
