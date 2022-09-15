from django.urls import path
from wishlist.views import show_wishlist, show_xml,show_json_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/<int:id>', show_json_id, name='show_json_id')
]