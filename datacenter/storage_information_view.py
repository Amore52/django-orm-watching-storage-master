from django.utils import timezone
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    active_visits = Visit.objects.filter(leaved_at=None)

    for visit in active_visits:
        owner_name = visit.passcard.owner_name
        entered_at = timezone.localtime(visit.entered_at)
        duration = visit.get_duration()
        is_strange = visit.is_visit_long()

        non_closed_visits.append({
            'who_entered': owner_name,
            'entered_at': entered_at.strftime('%d %B %Y г. %H:%M'),
            'duration': duration,
            'is_strange': is_strange
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
