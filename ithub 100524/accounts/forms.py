from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.urls import  reverse_lazy
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class CustomUserCreationForm(UserCreationForm):
    confirm = forms.BooleanField(required=True)

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "confirm",
        )

    def __init__(self, **kwargs):
        super(CustomUserCreationForm, self).__init__(**kwargs)
        terms_and_conditions = reverse_lazy("main:privacy_page")
        self.fields['confirm'].label = mark_safe((f"Я подтверждаю согласие на обработку персональных данных. <a href='{terms_and_conditions}'>Политика конфиденциальности</a>"))

    field_order = ['email',
                   'password1',
                   'password2',
                   'confirm',
                   ]

    def clean(self):
        cleaned_data = super().clean()
        confirm = cleaned_data.get('confirm')

        if not confirm:
            raise ValidationError('Требуется подтвердить согласие на обработку персональных данных')


class CustomUserCompleteForm(ModelForm):
    date_of_birth = forms.DateField(label='Дата рождения', required=False,
                                    input_formats=['%d/%m/%Y'],
                                    widget=forms.DateInput(
                                        format='%d/%m/%Y',
                                        attrs={
                                            'type': 'date_mod'}))

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'surname',
            'last_name',
            'sex',
            'date_of_birth',
            'citizenship',
            'region',
            'phone',
            'image_profile',
        ]

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name:
            return first_name.capitalize()
        return first_name

    def clean_surname(self):
        surname = self.cleaned_data.get('surname')
        if surname:
            return surname.capitalize()
        return surname

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name:
            return last_name.capitalize()
        return last_name
