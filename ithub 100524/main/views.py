from django.conf import settings
from django.shortcuts import render, redirect
from django.utils import timezone

from activities.models import Activities
from core.utils import send_telegram_message, get_client_ip
from main.forms import FeedbackCreateForm
from news.models import News


def index(request):
    form = FeedbackCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            object_form = form.save(commit=False)
            if request.user.is_authenticated:
                object_form.user = request.user
            object_form.ip_address = get_client_ip(request)
            try:
                send_telegram_message(settings.BOT_TOKEN,
                                      settings.BOT_SEND_TO_CHAT,
                                      message=( # max length 4096
                                          f"Письмо от {object_form.email[:100]}"
                                          "\n"
                                          f"Тема:  {object_form.subject[:100]}"
                                          "\n"
                                          f"Ip адрес:  {object_form.ip_address[:1000]}"
                                          "\n"
                                          f"Сообщение:  {object_form.content[:3500]}"
                                      ))
            except Exception as e:
                print(e)
                print('В телеграм не отправлено')
            object_form.save()
            return redirect('main:home')
    news = News.objects.filter(datetime_pub__lte=timezone.now())

    activities = Activities.objects.filter(datetime_pub__lte=timezone.now())

    context = {
        'news': news,
        'form': form,
        'activities_list': activities
    }
    return render(request, 'public/main/index.html', context)


def privacy(request):
    return render(request, 'public/main/privacy.html')
