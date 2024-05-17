from activities.models import StatusParticipation


def enum_activities_processor(request):
    return {
        'enum_activities': StatusParticipation.choices
    }
