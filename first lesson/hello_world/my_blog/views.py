from django.shortcuts import render
from my_blog.forms import SendMesgForm
from my_blog.models import SendMesg
from my_blog.models import CreateArticle
from my_blog.forms import CreateArticleForm
import math
# Create your views here.
def blog_url(request):
    if request.method == 'POST':
        data_form = SendMesgForm(data = request.POST)
        if data_form.is_valid():
            first_name = data_form.cleaned_data['first_name']
            last_name = data_form.cleaned_data['last_name']
            email = data_form.cleaned_data['email']
            message = data_form.cleaned_data['message']
            allow_mailing = data_form.cleaned_data['allow_mailing']
            about_object = SendMesg(first_name = first_name, last_name = last_name,
            email = email, message = message, allow_mailing = allow_mailing)
            about_object.save()
            

    form = SendMesgForm()
    about_data = SendMesg.objects.all()
    return render(request, "main.html", {'form':form, 'data': about_data})
def create_artc_url(request):
    if request.method == "POST":
        article_form = CreateArticleForm(request.POST,request.FILES)
        if article_form.is_valid():
            article_form.save()
        #else:
         #   print('Article form', article_form.errors)    
    artc_form = CreateArticleForm()
    create_article_data = CreateArticle.objects.all()
    return render(request, 'create_article.html', {'form':artc_form, 'data':create_article_data})    

def index(request, page=1):
    items_per_page = 10
    offset = items_per_page * (page-1)
    articles = CreateArticle.objects.all().order_by('-created_date')
    articles_count = articles.count()
    pages_range = range(1, int(math.ceil(articles_count/items_per_page)))
    return render(request, 'index.html', {'articles': articles[offset: items_per_page*page],
    'articles_count': articles_count,
    'pages_range':pages_range})

def article_single(request, id):
    print('article_single id {0}'.format(id))
    article_obj = CreateArticle.objects.get(id = id)
    context = {'article':article_obj}
    return render (request, 'article_single.html', context)



