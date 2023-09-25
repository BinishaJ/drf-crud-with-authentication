from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path("api-overview/", views.apiOverview, name="api-overview"),

    # books
    path("book-list", views.bookList, name="book-list"),
    path("book-read/<int:pk>", views.bookRead, name="book-read"),
    path("book-create", views.bookCreate, name="book-create"),
    path("book-update/<int:pk>", views.bookUpdate, name="book-update"),
    path("book-delete/<int:pk>", views.bookDelete, name="book-delete"),

    #authors
    path("author-list", views.authorList.as_view(), name="author-list"),
    path("author-read/<int:pk>", views.authorRead, name="author-read"),
    path("author-create", views.authorCreate.as_view(), name="author-create"),
    path("author-update/<int:pk>", views.authorUpdate, name="author-update"),
    path("author-delete/<int:pk>", views.authorDelete, name="author-delete"),

    #token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
