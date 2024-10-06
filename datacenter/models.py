from datetime import timedelta
from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        if self.leaved_at is None:
            time_leave = timezone.localtime(timezone.now())
        else:
            time_leave = timezone.localtime(self.leaved_at)
        time_enter = timezone.localtime(self.entered_at)
        time_duration = time_leave - time_enter
        cleaned_duration = timedelta(seconds=time_duration.seconds)
        return cleaned_duration

    def is_visit_long(self):
        duration = self.get_duration()
        return duration > timedelta(hours=1)

    def is_strange_card(self):
        if self.leaved_at is None:
            return None

        time_enter = timezone.localtime(self.entered_at)
        time_leave = timezone.localtime(self.leaved_at)
        time_duration = time_leave - time_enter
        return time_duration > timedelta(hours=1)






