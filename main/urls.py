from django.urls import path
from main.views import show_main
from main.views import create_product
from main.views import show_xml
from main.views import show_json
from main.views import show_xml_by_id
from main.views import show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import delete_data
from main.views import increase_amount
from main.views import decrease_amount
from main.views import edit_product
from main.views import delete_product
from main.views import get_product_json
from main.views import add_product_ajax
from main.views import search_item
from main.views import create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<int:id>', delete_data, name='delete_data'),
    path('increase/<int:id>/', increase_amount, name='increase_amount'),
    path('decrease/<int:id>/', decrease_amount, name='decrease_amount'),
    path('edit/<int:id>/', edit_product, name='edit_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('search/', search_item, name='search_item'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]