from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect

from polls.models import Post
from polls.forms import PostForm
from polls.models import Good


def index(request):
    # POSTでデータを送信
    if request.method == 'POST':
        form = PostForm(request.POST)
    # 値にエラーがないか確認
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    posts = Post.objects.order_by('-created_at')
    paginator = Paginator(posts, 5)

    page = request.GET.get('page', 1)
    posts = paginator.page(page)

    good_count = Good.objects.count()

    return TemplateResponse(request,
                            'polls/index.html',
                            {'posts': posts,
                             'form': form,
                             'good_count': good_count})


def good(request, post_id):
    if request.method == 'POST':
        Good.objects.create(post_id=post_id)

        return redirect('index')
