from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^update$', views.update, name='update'),
        url(r'^login$', views.user_login, name='login'),
        url(r'^logout$', views.user_logout, name='logout'),
        url(r'^project$', views.project, name='project'),
        url(r'^job', views.job, name='job'),
        url(r'^resetpassword$', views.resetpassword, name='resetpassword'),
        ]
