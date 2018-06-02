from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    # /shop/
    url(r'^$', views.IndexView.as_view(), name = 'index'),
]