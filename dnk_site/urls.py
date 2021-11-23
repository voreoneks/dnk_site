"""dnk_site URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from news.views import *
from release.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutPage.as_view(), name='logout'),
    path('', MainPage, name='main'),
    path('news/', include('news.urls')),
    path('release/', include('release.urls')),
    path('documents/', include('documents.urls')),
    path('marketing/', include('marketing.urls')),
    path('myaccount/', include('lk.urls')),
    path('calc/', include('calc.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)

    # urlpatterns = [
    #     path('__debug__/', include(debug_toolbar.urls)),
    # ] + urlpatterns
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
