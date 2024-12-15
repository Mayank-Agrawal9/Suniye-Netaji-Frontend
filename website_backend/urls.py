"""
URL configuration for website_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from website_backend import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path("api/", include('cms.urls')),


]

admin.sites.AdminSite.site_header = 'Suniye Netaji Website Admin'
admin.sites.AdminSite.site_title = 'Suniye Netaji Website Admin'
admin.sites.AdminSite.index_title = 'Suniye Netaji Website administration'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

try:
    if settings.ON_DEVELOPMENT:
        urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
except:
    pass