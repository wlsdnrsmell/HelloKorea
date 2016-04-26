from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.post_list, name = 'post_list'),
    #문자열 표현하는 정결표현 
    url(r'^(?P<pk>\d+)/$',views.post_detail, name = 'post_detail'),      
]