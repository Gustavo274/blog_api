from django.contrib.auth import get_user_model
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from articles.permissions import IsOwner
from .serializers import UserSerializer

User = get_user_model()


class UserCreate(CreateAPIView):

    #View responsável por criar um novo usuário.

    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class UserList(ListAPIView):

    #View responsável por listar os usuários já criados.

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):

    #View responsável por detalhar um usuário em específico.

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'