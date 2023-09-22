from django.urls import path
from .views import NewsList, Mysearch, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView
# создаем локальный список адресов
urlpatterns = [

path('', NewsList.as_view()),
path('search/', Mysearch.as_view()), # ссылка на поиск
path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # Ссылка на просмотр новости №
path('create/', NewsCreateView.as_view(), name='news_create'),  # Ссылка на создание новости
path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),  # Ссылка на удаление новости №
path('create/<int:pk>', NewsUpdateView.as_view(), name='news_create'),  # Ссылка на редактирование новости №

]