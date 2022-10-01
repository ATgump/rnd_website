from django.shortcuts import render, get_object_or_404
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  DeleteView)
from .models import Article

# def blog_home_view(request):
#     queryset = Article.objects.all()
#     context={
#         "object_list":queryset
#     }
#     return render(request,"Article/article_list.html",context=context)


class ArticleListView(ListView):
    template_name: str = "Article/article_list.html"
    queryset = Article.objects.all()


# def blog_article_view(request,id):
#     obj = get_object_or_404(Article,id=id)
#     context = {
#         "obj":obj
#     }
#     return render(request,"Article/article_detail.html",context=context)


class ArticleDetailView(DetailView):
    template_name: str = "Article/article_detail.html"
    queryset = Article.objects.all()
