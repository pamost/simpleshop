from django.conf.urls import url
from orders import views


urlpatterns = [
    url(r'^cart_adding/$', views.cart_adding, name='cart_adding')
]
