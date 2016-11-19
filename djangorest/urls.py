from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
# from rest_framework.urlpatterns import  format_suffix_patterns
# from stockapi import views

urlpatterns = patterns('',
      url(r'^expensetracker/', include('expense_tracker.urls')),
      url(r'^stockapi/', include('stockapi.urls')),
      url(r'^admin/', include(admin.site.urls)),
     # url(r'^stocks/',StockList.as_view() ),
)


#urlpatterns = format_suffix_patterns(urlpatterns)