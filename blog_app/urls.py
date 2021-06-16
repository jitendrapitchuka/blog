from django.conf.urls import url
from . import views

urlpatterns={
    url('',views.PostListView.as_view(),name='post_list'),

    url('/about',views.Aboutview.as_view(),name='about'),
    url('post/<int:pk>',views.PostDetailview.as_view(),name='Post_detail'),
    url('post/new',views.CreatePostView.as_view(),name='post_new'),
    url('post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_edit'),
    url('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post_remove'),
    url('drafts/',views.DraftListView.as_view(),name='post_draft_list')
}