from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class News(models.Model):
    title = models.CharField('Название', max_length=150)
    anons = models.CharField('Анонс', max_length=150)
    full_text = models.TextField('Статья')
    datetime_pub = models.DateTimeField('Дата публикации')
    views = models.IntegerField('Просмотры', default=0)
    image = models.ImageField(
        'Изображение', upload_to='news/', blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name='Автор'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:detail_news", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
