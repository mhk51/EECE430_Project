from django.conf.urls import url
from nBookapp.views import bookList_U
from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
    
)

app_name = 'cart'

urlpatterns = [
    url(r'^add_to_cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order_summary/$', order_details, name="order_summary"),
    # url(r'^success/$', success, name='purchase_success'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^checkout/$', checkout, name='checkout'),
    
]