"""expence URL Configuration

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
from django.urls import path
# from django.conf.urls import url
from application import views
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register("bank",views.AccountViewSet)
# router.register('bankbalance/',views.total_amount)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.htmlPage),
    # url('about', views.about,name='about'),
    path("expense/",views.expenseApiView.as_view()),
    path("",include(router.urls)),
    path("bankbalance/",views.total_amount,name='total_amount')
    # parth("")

]
