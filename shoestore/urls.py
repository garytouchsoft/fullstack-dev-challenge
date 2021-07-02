
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view'),
    url(r'^order/$', views.OrderView.as_view(), name='order_view'),
    url(r'^ordersummary/$', views.SummaryView.as_view(), name='summary_view'),
    url(r'^ordersummary/(?P<order_pid>[0-9]+)/$', views.SummaryView.as_view()),
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
