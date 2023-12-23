from django.urls import path, include
from . import views



# Главная
urlpatterns = [
    path('', views.index, name= 'index')
] 


# Регистрация пользователя

urlpatterns += [
    path('register/', views.RegisterUser.as_view(), name='register'),
]


# Профиль пользователя 

urlpatterns += [
    path('profile/', views.ProfileUser, name='profile'),
]

# Добавление, удаление книги в профиль

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
urlpatterns += [
    path('profile/<int:pk>/add/', views.AddBookProfile.as_view(), name='add_profile_book'),
    path('profile/<int:pk>/delete/', views.DeleteBookProfile.as_view(), name='delete_profile_book'),
]



# Книги (Список, Детальная информация)

urlpatterns += [
    path('book/', views.BookListView.as_view(), name='book'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]



# Авторы (Список, Детальная информация)


urlpatterns += [
    path('author/', views.AuthorListView.as_view(), name='author'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
]



# Коментарии книги

urlpatterns += [
    path('reviews/<int:pk>/', views.AddComment.as_view(), name='book_comment')
]


# Редактирование книг (Создание, Изменение, Удаление)
urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]


# Редактирование автора (Создание, Изменение, Удаление)

urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]



# Фильтрация по жанрам

urlpatterns +=[
    path('genre_list/<int:pk>/', views.FilterBook.as_view(), name='genre_list')
]



# Поиск по имени

urlpatterns += [
    path('search/', views.Search.as_view(), name='search')
]


