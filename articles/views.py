from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .pagination import ArticleLimitOffsetPagination
from .models import Article, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    CommentSerializer,
    CommentCreateSerializer,
    ArticleCreateSerializer,
    ArticleListSerializer,
    ArticleDetailSerializer,
)

from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def ApiOverview(request):

    #Home da api, com uma overview dos path para facilitar a navageação.

    api_urls = {
        'all_articles': '/articles/',
        'Create article': '/articles/create',
        'Article detail': '/articles/pk/',
        'Create comment for article': '/articles/pk/comment/create',
        'Comment detail': '/articles/pk/comment/id',
        'Register user': '/user/register',
        'User detail': '/user/pk',
        'all_users': '/user/'
    }
  
    return Response(api_urls)


class CreateArticleView(APIView):

    #View responsável por criar um artigo através do método post. Retorna a data dos artigos criados. Parâmetros utilizados: [title, subtitle, content, keyword]


    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ListArticleView(ListAPIView):

    #View responsável por fazer uma listagem dos artigos já criados através do método get.
    
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ArticleLimitOffsetPagination


class DetailArticleView(RetrieveUpdateDestroyAPIView):

    #View responsável por detalhar um artigo específico através de um método Get. Além disso artravés dessa view é possível deletar e atualizar um artigo.

    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CreateCommentView(APIView):

    #View responsável por criar um comentário através do método post. Retorna a data dos comentário criado. Parâmetros utilizados: [body]

    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, parent=article)
            return Response(serializer.data, status=200)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ListCommentView(APIView):

    #View responsável por fazer uma listagem dos comentários já criados através do método get.

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        comments = Comment.objects.filter(parent=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)


class DetailCommentView(RetrieveUpdateDestroyAPIView):

    #View responsável por detalhar um comentário específico através de um método Get. Além disso artravés dessa view é possível deletar e atualizar um comentário.

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Comment.objects.all()
    lookup_fields = ["parent", "id"]
    serializer_class = CommentCreateSerializer