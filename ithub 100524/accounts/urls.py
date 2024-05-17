from django.urls import include, path

from accounts.views import SignupPageView, personal_profile

app_name = 'accounts'
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("me/", personal_profile, name="personal_profile"),
]
