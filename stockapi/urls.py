from django.conf.urls import patterns, url
from stockapi.views import StockList

urlpatterns = patterns('',
      url(r'^stock/',StockList.as_view(), name= "stock" ),
)
