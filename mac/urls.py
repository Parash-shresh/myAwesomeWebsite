"""mac URL Configuration

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
from xml.dom.minidom import Document

from django.urls import path, include
from django.contrib import admin
#after adding MEDIA_ROOT and MEDIA_URLS in settings.py we need to import it
from django.conf import settings #for testing media folder 
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('includeExample/', include('shop.urls_Example')),
    #path('DeleteAfterLearning/', include('shop.urls_Example')),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('shop/productList', include('shop.urls'))
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#yo mathi ko static wala code le image lai base dir ko media vanne folder ma admin le haleko image haru upload gardinxa,,,settings.py ma ni 2 ota line add gareko xa media_root ra media_urls vanne gayera herda hunxa