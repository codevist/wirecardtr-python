"""wirecard_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    
    url(r'^$', BasicApi, name='BasicApi'),
    url(r'^ApiPlus/', ApiPlus, name='ApiPlus'),
    url(r'^ProApi/', ProApi, name='ProApi'),
    url(r'^MarketPlaceDeactiveSubPartner/', MarketPlaceDeactiveSubPartner, name='MarketPlaceDeactiveSubPartner'),
    url(r'^SendInformationSmsService/', SendInformationSmsService, name='SendInformationSmsService'),
    url(r'^SelectSubscriber/', SelectSubscriber, name='SelectSubscriber'),
    url(r'^SelectSubscriberDetail/', SelectSubscriberDetail, name='SelectSubscriberDetail'),
    url(r'^MarketPlaceAddSubPartner/', MarketPlaceAddSubPartner, name='MarketPlaceAddSubPartner'),
    url(r'^MarketPlaceUpdateSubPartner/', MarketPlaceUpdateSubPartner, name='MarketPlaceUpdateSubPartner'),
    url(r'^DeactivateSubscriber/', DeactivateSubscriber, name='DeactivateSubscriber'),
    url(r'^MarketPlaceSale3DSec/', MarketPlaceSale3DSec, name='MarketPlaceSale3DSec'),
    url(r'^MarketPlaceMPSale/', MarketPlaceMPSale, name='MarketPlaceMPSale'),
    url(r'^MarketPlaceReleasePayment/', MarketPlaceReleasePayment, name='MarketPlaceReleasePayment'),
    url(r'^CCProxySale/', CCProxySale, name='CCProxySale'),
    url(r'^CCProxySale3D/', CCProxySale3D, name='CCProxySale3D'),
    url(r'^WDTicketSale3DURLProxy/', WDTicketSale3DURLProxy, name='WDTicketSale3DURLProxy'),
    url(r'^WDTicketSaleURLProxy/', WDTicketSaleURLProxy, name='WDTicketSaleURLProxy'),
    url(r'^TransactionQueryByOrderId/', TransactionQueryByOrderId, name='TransactionQueryByOrderId'),
    url(r'^TransactionQueryByMPAY/', TransactionQueryByMPAY, name='TransactionQueryByMPAY'),
    
    url(r'^success/', success, name='success'),
    url(r'^fail/', fail, name='fail'),
    
]
