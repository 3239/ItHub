from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('privacy/', TemplateView.as_view(template_name='public/main/privacy.html'), name='privacy_page'),
]