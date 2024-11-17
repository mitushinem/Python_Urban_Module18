from django.urls import path
from . import views
from task4.views import index, game, cart

urlpatterns = [
    path('', index),
    path('shop/', game),
    path('cart/', cart),
    path('reg/', views.sign_up_by_html),
    path('reg_c/', views.sign_up_by_django),
]