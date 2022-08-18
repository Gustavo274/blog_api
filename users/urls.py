from django.urls import path
from .views import UserCreate, UserList, UserDetail

app_name = "users"

urlpatterns = [
    path("", UserList.as_view(), name="user_list"),
    path("register/", UserCreate.as_view(), name="user_create"),
    path("<int:id>/", UserDetail.as_view(), name="user_detail"),
]