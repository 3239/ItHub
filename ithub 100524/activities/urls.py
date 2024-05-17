from django.urls import path, include
from . import views
app_name = 'activities'

urlpatterns_staff = [
    path('list_activities/', views.list_activities_staff, name='list_activities_staff'),
    path('detail_news/<int:pk>/', views.detail_activities_staff, name='detail_activities_staff'),
    path('create_activities/', views.create_activities_staff, name='create_activities_staff'),
    path('update_activities/<int:pk>/', views.update_activities_staff, name='update_activities_staff'),
    path('delete_activities/<int:pk>/', views.delete_activities_staff, name='delete_activities_staff'),

    path('list_requests_activities_staff/', views.list_requests_activities_staff, name='list_requests_activities_staff'),
    path('change_status_activities_staff/<int:pk>/', views.change_status_activities_staff, name='change_status_activities_staff'),
]

urlpatterns_user = [
    path('registration_activities/', views.registration_activities, name='registration_activities'),
    path('my_requests_activities/', views.my_requests_activities, name='my_requests_activities'),
]

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail_activities'),
    path('staff/', include(urlpatterns_staff)),
    path('user/', include(urlpatterns_user)),
]
