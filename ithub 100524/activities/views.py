from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from activities.forms import ActivitiesForm, ActivitiesRegistrationForm, ChangeStatusParticipationActivitiesForm
from activities.models import Activities, ParticipationActivities, StatusParticipation


def detail(request, pk):
    activities_obj = get_object_or_404(Activities, pk=pk)

    activities_obj.views += 1
    activities_obj.save()

    context = {'activities_obj': activities_obj}
    return render(request, 'public/activities/detail.html', context)


@login_required
def registration_activities(request):
    form = ActivitiesRegistrationForm(
        request.POST or None,
        user=request.user
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('activities:my_requests_activities')

    return render(request, 'user/activities/registration_activities.html', {'form': form})


@login_required
def my_requests_activities(request):
    my_requests = ParticipationActivities.objects.filter(created_by=request.user)
    return render(request, 'user/activities/my_requests_activities.html', {'my_requests': my_requests})


@staff_member_required
def list_activities_staff(request):
    activities = Activities.objects.all()
    context = {'activities_list': activities}
    return render(request, 'staff/activities/list.html', context)


@staff_member_required
def detail_activities_staff(request, pk):
    activities_obj = get_object_or_404(Activities, id=pk)
    context = {'activities_obj': activities_obj}
    return render(request, 'staff/activities/detail.html', context)


@staff_member_required
def create_activities_staff(request):
    form = ActivitiesForm(
        request.POST or None,
        files=request.FILES or None,
        user=request.user
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('activities:list_activities_staff')

    return render(request, 'staff/activities/create_edit.html', {'form': form})


@staff_member_required()
def update_activities_staff(request, pk):
    activities_obj = get_object_or_404(Activities, id=pk)

    form = ActivitiesForm(
        request.POST or None,
        files=request.FILES or None,
        user=request.user,
        instance=activities_obj
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('activities:detail_activities_staff', pk=pk)

    context = {
        'is_edit': True,
        'form': form,
    }
    return render(request, 'staff/activities/create_edit.html', context)


@staff_member_required
def delete_activities_staff(request, pk):
    activities_obj = get_object_or_404(Activities, id=pk)
    activities_obj.delete()
    return redirect('activities:list_activities_staff')


@staff_member_required
def list_requests_activities_staff(request):
    requests_activities = ParticipationActivities.objects.all()
    q = request.GET.get('q')
    human_value_q = dict(StatusParticipation.choices).get(q)
    if human_value_q:
        requests_activities = requests_activities.filter(status=q)
    context = {
        'form': ChangeStatusParticipationActivitiesForm(),
        'requests_activities': requests_activities,
        'human_value_q': human_value_q
    }
    return render(request, 'staff/activities/list_requests.html', context)


@staff_member_required
def change_status_activities_staff(request, pk, ):
    obj = get_object_or_404(ParticipationActivities, pk=pk)
    if request.method == 'POST':
        form = ChangeStatusParticipationActivitiesForm(request.POST, instance=obj)
        if form.is_valid():
            obj.save()
    return redirect('activities:list_requests_activities_staff')
