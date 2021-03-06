"""BidDing URL Configuration

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
from mainpage.views import ShowHomePage
from mainpage.views import Login
from mainpage.views import Logout
from mainpage.views import ShowUserHomePage
from mainpage.views import ShowUserBiddingPage
from mainpage.views import ShowUserSubmitPage
from mainpage.views import ShowUserInfoPage
from django.conf.urls import include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^$',ShowHomePage),
    url(r'^login/',Login),
    url(r'^logout/',Logout),
    url(r'userHome/',ShowUserHomePage),
    url(r'bidding/',ShowUserBiddingPage),
    url(r'submit/',ShowUserSubmitPage),
    url(r'userInfo/',ShowUserInfoPage),
]
