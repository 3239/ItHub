from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserCompleteForm

User = get_user_model()


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("main:home")
    template_name = "registration/signup.html"


@login_required
def personal_profile(request):
    form = CustomUserCompleteForm(request.POST or None,
                                  files=request.FILES or None,
                                  instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('accounts:personal_profile', )
    context = {'user_profile': request.user,
               'form': form}

    if request.user.is_staff:
        return render(request, 'staff/accounts/me_staff.html', context)
    return render(request, 'user/accounts/me_base.html', context)
