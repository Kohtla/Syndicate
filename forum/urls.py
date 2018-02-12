from django.conf.urls import url
from . import views

app_name = 'forum'

urlpatterns = [
    # /forum/
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    # /forum/
    url(r'^register/$', views.UserFormView.as_view(), name = 'register'),
    # /forum/3
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
    # /forum/theme/add/*
    url(r'theme/add/$', views.ThemeCreate.as_view(), name = 'theme-add'),

    url(r'^logout/$', views.Log_out.as_view(), name = 'logout'),

    url(r'^login/$', views.Log_in.as_view(), name='login'),



]
