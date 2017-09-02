"""borrowCyborrow URL Configuration

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

from borrow.views import borrowPageView, borrowView
from buy.views import buyPageView,buyView
from home.views import HomePage
#from sell.views import sellView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomePage.as_view(),name='home'),
    url(r'^borrow$',borrowPageView.as_view(),name='borrow-page'),
    url(r'^borrow/(?P<cid>[.\-_\w]+)/$', borrowView.as_view(), name='borrow'),
    url(r'^buy$', buyPageView.as_view(), name='buy-page'),
    url(r'^buy/(?P<cid>[.\-_\w]+)/$', buyView.as_view(), name='buy'),
    #url(r'^sell$',sellView.as_view(),name='sell-view'),
]