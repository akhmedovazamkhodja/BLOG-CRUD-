from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_func, name='posts_func'),
    path('<slug>/', post_detail, name='post_detail')
]