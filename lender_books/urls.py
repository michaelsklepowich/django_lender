from .views import books_list_view, books_detail_view
from django.urls import path


urlpatterns = [
    path('', books_list_view, name='books_list'),
    path('<int:pk>', books_detail_view, name='books_detail'),
]