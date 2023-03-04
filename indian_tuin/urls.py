"""indian_tuin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from menu.views import handler404, handler500, handler403
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('blog/', include('blog.urls'), name='blog'),
    path('summernote/', include('django_summernote.urls')),
    path('menu/', include('menu.urls')),
    path("accounts/", include("allauth.urls")),
    path("users/", include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path('404/', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')},),
        path('500/', default_views.server_error),
        path('403/', default_views.permission_denied, kwargs={'exception': Exception('Access Denied')}),

    ]
else:
    urlpatterns += [
        path('404/', handler404),
        path('500/', handler500),
        path('403/', handler403),
    ]
