from django.contrib import admin
from django.urls import path, include
from articles import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # home
    path('', views.ApiOverview, name='home'),

    # Login pelo browser
    path("api-auth/", include("rest_framework.urls")),

    # Autenticação da api
    path("user/", include("users.urls", namespace="users")),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Api
    path("articles/", include("articles.urls", namespace="articles_api")),
]
