from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # home
    path('', views.ApiOverview, name='home'),

    # Login pelo browser
    path("api-auth/", include("rest_framework.urls")),

    # Autenticação da api
    path("user/", include("users.urls", namespace="users")),


    # Api
    path("articles/", include("articles.urls", namespace="articles_api")),
]
