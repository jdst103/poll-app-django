"""poll_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#added
from django.urls import path

#import urls
from poll import views as poll_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('home_json/', poll_views.Poll_json.home_json, name='home_json'),
    path('results_json/<poll_id>/', poll_views.Poll_json.results_json, name='results_json'),
    path('', poll_views.Poll.poll_list, name='home'),
    # path('create/', poll_views.Poll.create, name='create'),
    path('vote/<poll_id>/', poll_views.Poll.vote, name='vote'),
    path('results/<poll_id>/', poll_views.Poll.poll_detail, name='results'),
]
