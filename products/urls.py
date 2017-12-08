from django.conf.urls import url
from products import views


urlpatterns = [
    url('^product/(?P<product_id>\w+)/$', views.product, name='product')
]
