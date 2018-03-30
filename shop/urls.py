from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    # /shop/
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    # /shop/3
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "product_detail"),



]
