from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect

from news.forms import NewsForm
from news.models import News


def index(request):
    news = News.objects.all()
    context = {'news_list': news}
    return render(request, 'public/news/index.html', context)


def detail(request, pk):
    news = get_object_or_404(News, pk=pk)

    news.views += 1
    news.save()

    context = {'news_detail': news}
    return render(request, 'public/news/detail.html', context)


@staff_member_required
def list_news_staff(request):
    news = News.objects.all()
    context = {'news_list': news}
    return render(request, 'staff/news/list.html', context)


@staff_member_required
def detail_news_staff(request, pk):
    news_obj = get_object_or_404(News, id=pk)
    context = {'article': news_obj}
    return render(request, 'staff/news/detail.html', context)


@staff_member_required
def create_news_staff(request):
    form = NewsForm(
        request.POST or None,
        files=request.FILES or None,
        user=request.user
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('news:list_news_staff')

    return render(request, 'staff/news/create_edit.html', {'form': form})


@staff_member_required()
def update_news_staff(request, pk):
    news_obj = get_object_or_404(News, id=pk)

    form = NewsForm(
        request.POST or None,
        files=request.FILES or None,
        user=request.user,
        instance=news_obj
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('news:detail_news_staff', pk=pk)

    context = {
        'is_edit': True,
        'form': form,
    }
    return render(request, 'staff/news/create_edit.html', context)


@staff_member_required
def delete_news_staff(request, pk):
    news_obj = get_object_or_404(News, id=pk)
    news_obj.delete()
    return redirect('news:list_news_staff')
