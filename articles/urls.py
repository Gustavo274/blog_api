from django.urls import path
from .views import (
    CreateArticleView,
    ListArticleView,
    DetailArticleView,
    CreateCommentView,
    ListCommentView,
    DetailCommentView,
)
from . import views

app_name = "articles"

urlpatterns = [
    path("", ListArticleView.as_view(), name="list_article"),
    path("create/", CreateArticleView.as_view(), name="create_article"),
    path("<int:pk>/", DetailArticleView.as_view(), name="article_detail"),
    path("<int:pk>/comment/", ListCommentView.as_view(), name="list_comment"),
    path(
        "<int:pk>/comment/create/",
        CreateCommentView.as_view(),
        name="create_comment",
    ),
    path(
        "<int:pk>/comment/<int:id>/",
        DetailCommentView.as_view(),
        name="comment_detail",
    ),
]