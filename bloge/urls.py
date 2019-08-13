from django.urls import path
from .import views

urlpatterns = [
    #http://127.0.0.1:8000/
    path('', views.post_list, name='post_list'),

    #http://127.0.0.1:8000/post/2
    path('post/<int:pk>/', views.post_detail, name="post_detail"),

    #http://127.0.0.1:8000/post/new
    path('post/new/', views.post_new, name='post_new')
]
