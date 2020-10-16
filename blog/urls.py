from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/new/', views.post_new, name='post_new'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/drafts/', views.post_draft, name='post_draft'),
    path('blog/post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('blog/post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('blog/post/<int:pk>/comment.', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
