"""hello_world URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from my_app.views import index
from test_form.views import form_url
from calculator.views import calc_form_url
from my_blog.views import blog_url
from my_blog.views import create_artc_url
from my_blog.views import index
from my_blog.views import article_single
urlpatterns = [
    path('',index, name='main_page'),
    path('<int:page>', index, name='main_page'),
    path('templates/article_single/<int:id>/', article_single, name='article_single'),
    path('templates/index/', blog_url, name='about'),
    path('templates/create_article',create_artc_url, name="create_article"),
    path('admin/', admin.site.urls),
    path('', index)
    #path('test_form', form_url),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


