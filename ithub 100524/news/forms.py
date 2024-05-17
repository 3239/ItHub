import datetime

from django import forms
from django.forms import ModelForm
from django.utils import timezone

from news.models import News


class NewsForm(ModelForm):
    date_pub = forms.DateField(
        label='Дата публикации',
        required=True,
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'type': 'date_mod'})
    )

    time_pub = forms.TimeField(
        label='Время публикации',
        required=True,
        input_formats=['%H:%M'],
        widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'})
    )

    class Meta:
        model = News
        fields = ['title', 'anons', 'full_text', 'image']

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        instance = kwargs.get('instance', None)
        if instance is not None:
            date_pub = instance.datetime_pub
            if date_pub:
                # Set initial values for the date and time fields
                self.fields['date_pub'].initial = date_pub.date()
                self.fields['time_pub'].initial = date_pub.time()


    def save(self, commit=True):
        instance = super().save(commit=False)
        date_pub = self.cleaned_data['date_pub']
        time_pub = self.cleaned_data['time_pub']
        datetime_pub = datetime.datetime.combine(date_pub,
                                                 time_pub)
        if timezone.is_naive(datetime_pub):
            datetime_pub = timezone.make_aware(datetime_pub, timezone.get_current_timezone())
        instance.datetime_pub = datetime_pub
        instance.author = self.user
        if commit:
            instance.save()
        return instance
