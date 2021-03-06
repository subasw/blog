from django.urls import path
from .import views


urlpatterns = [
    #http://127.0.0.1:8000/
    path('', views.post_list, name='post_list'),

    #http://127.0.0.1:8000/post/2
    path('post/<int:pk>/', views.post_detail, name="post_detail"),

    #http://127.0.0.1:8000/post/new
    path('post/new/', views.post_new, name='post_new'),

    #http://127.0.0.1:8000/post/2/edit
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    #http://127.0.0.1:8000/post/2/delete
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    #http://127.0.0.1:8000/draft
    path('draft/', views.post_draft, name='post_draft'),

    #http://127.0.0.1:8000/post/2/publish
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),

    #http://127.0.0.1:8000/accounts/login this path included to the urls


    #http://127.0.0.1:8000/post/2/comment
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),


    #http://127.0.0.1:8000/comment/3/remove
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    #http://127.0.0.1:8000/comment/3/approve
    path('comment/<int:pk>/approve', views.comment_approve, name='comment_approve'),

    #http://127.0.0.1:8000/signup
    path('signup/', views.signup, name='signup'),
]
