from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from blog.models import Article

# Create your views here.
class list(generic.ListView):
    model=Article
    template_name='article_list.html'
    
    def get(self, request, *args, **kwargs):
        

        articles = Article.objects.all().order_by('-created_at')
        context = {
            'articles': articles
        }
        return render(request,'blog/article_list.html', context)
