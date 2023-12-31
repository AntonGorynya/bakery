"""bakeryshop URL Configuration

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
from cakeorder import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('index.html', views.index, name='index'),
    path('lk', views.lk, name='lk'),
    path('sync/', views.sync_click, name='sync_click'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('reg', views.reg_page, name='reg'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
