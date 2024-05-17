from django.urls import path, include
from . import views

app_name = 'news'

urlpatterns_staff = [
    path('list_news/', views.list_news_staff, name='list_news_staff'),
    path('detail_news/<int:pk>/', views.detail_news_staff, name='detail_news_staff'),
    path('create_news/', views.create_news_staff, name='create_news_staff'),
    path('update_news/<int:pk>/', views.update_news_staff, name='update_news_staff'),
    path('delete_news/<int:pk>/', views.delete_news_staff, name='delete_news_staff'),
]
urlpatterns = [
    path('', views.index, name='list_news'),
    path('<int:pk>/', views.detail, name='detail_news'),
    path('staff/', include(urlpatterns_staff)),


]
