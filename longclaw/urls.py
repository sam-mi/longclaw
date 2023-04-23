from django.urls import include, path
from longclaw.basket import urls as basket_urls
from longclaw.checkout import urls as checkout_urls
from longclaw.shipping import urls as shipping_urls
from longclaw.orders import urls as order_urls

urlpatterns = [
    path(r'', include(basket_urls)),
    path(r'', include(checkout_urls)),
    path(r'', include(shipping_urls)),
    path(r'', include(order_urls)),
]
