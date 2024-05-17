from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse

from core.models import CreatedUpdatedModel

User = get_user_model()


class StatusParticipation(models.TextChoices):
    UNKNOWN = ("UNK", "На рассмотрении")
    ACCEPTED = ("ACC", "Принята")
    UNACCEPTED = ("UNA", "Отклонена")


class Activities(CreatedUpdatedModel):
    title = models.CharField('Название', max_length=150)
    anons = models.CharField('Анонс', max_length=150)
    full_text = models.TextField('Полный текст')
    datetime_pub = models.DateTimeField('Дата Мероприятия')
    views = models.IntegerField('Просмотры', default=0)
    image = models.ImageField(
        'Изображение', upload_to='activities/', blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='activities',
        verbose_name='Автор'
    )

    def __str__(self):
        return f"{self.title} Время: {self.datetime_pub.strftime('%d/%m/%Y %H:%M')}"

    def get_absolute_url(self):
        return reverse("activities:detail_activities", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class ParticipationActivities(CreatedUpdatedModel):
    first_name = models.CharField("Имя", max_length=100 )
    surname = models.CharField("Фамилия", max_length=100)
    last_name = models.CharField("Отчество", max_length=100)
    email = models.EmailField(max_length = 255, verbose_name = 'Емайл')

    activity = models.ForeignKey(
        Activities, verbose_name='Мероприятие',
        on_delete=models.CASCADE,
        related_name='participation_activities')
    created_by = models.ForeignKey(
        User, verbose_name='Участник',
        on_delete=models.CASCADE,
        related_name='participation_activities')
    education_entity = models.CharField('Образовательное учреждение',
                                        max_length=150,
                                        blank=True,
                                        null=True)
    status = models.CharField(
        max_length=3,
        choices=StatusParticipation.choices,
        default=StatusParticipation.UNKNOWN,
    )

    class Meta:
        verbose_name = 'Участие в мероприятии'
        verbose_name_plural = 'Участие в мероприятиях'
        constraints = [
            UniqueConstraint(
                fields=['activity', 'created_by'], name='unique_participation'),
        ]

    def __str__(self):
        return f'{self.activity} | {self.created_by} | {self.get_status_display()}'
