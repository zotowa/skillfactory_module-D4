from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView  # импортируем необходимые дженерики
from django.core.paginator import Paginator  # импортируем класс

from .models import News, Category
from .filters import NewsFilter
from .forms import NewsForm

class NewsList(ListView):
    model = News  # указываем модель
    template_name = 'news.html'  # указываем имя шаблона
    context_object_name = 'all_news'  # это имя списка
    ordering = ['-news_create_time']
    paginate_by = 7  # поставим постраничный вывод
    form_class = NewsForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())

        context['categories'] = Category.objects.all()
        context['form'] = NewsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму

        if form.is_valid():  # если пользователь ввёл всё правильно
            form.save()

        return super().get(request, *args, **kwargs)


# Дженерики

class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    queryset = News.objects.all()

class NewsCreateView(CreateView):
    template_name = 'news_create.html'
    form_class = NewsForm

class NewsUpdateView(UpdateView):
    template_name = 'news_create.html'
    form_class = NewsForm

    # метод get_object
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)

class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = News.objects.all()
    success_url = '/news/'

class Mysearch(ListView):
    model = News  # указываем модель
    template_name = 'search.html'  # указываем имя шаблона
    context_object_name = 'all_news'  # это имя списка
    ordering = ['-news_create_time']
    paginate_by = 7


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context