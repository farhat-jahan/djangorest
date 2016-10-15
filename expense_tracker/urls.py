from django.conf.urls import url
from django.conf.urls import patterns, include, url
from expense_tracker import views

urlpatterns = [
               url(r'^user/$',views.user_list),
               ]