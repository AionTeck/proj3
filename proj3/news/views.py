from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm
from django.shortcuts import get_object_or_404, redirect
from django.core.files.uploadedfile import SimpleUploadedFile
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
            is_published=True)


class ViewNews(DetailView):
    model = News
    # template_name = 'news/news_detail.html'
    # pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')

# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'List of news',
#     }
#     return render(request, 'news/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request,
#                   'news/category.html',
#                   {'news': news,
#                    'category': category},
#                   )


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {'news_item': news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             news = form.save()
#             return redirect('home')
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
