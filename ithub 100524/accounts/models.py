from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length = 255, unique = True, verbose_name = 'Емайл')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    GENDER_CHOICES = (
        ('M', 'М'),
        ('F', 'Ж'),
    )

    first_name = models.CharField("Имя",max_length=100, null=True, blank=True)
    surname = models.CharField("Фамилия",max_length=100, null=True, blank=True)
    last_name = models.CharField("Отчество",max_length=100, null=True, blank=True)
    phone = models.CharField("Номер телефона учащегося",max_length=20, null=True, blank=True)
    sex = models.CharField("Пол",max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField('Дата рождения',null=True, blank=True)
    citizenship = models.CharField("Гражданство",max_length=100, null=True, blank=True)
    region = models.CharField("Регион",max_length=100, null=True, blank=True)
    image_profile = models.ImageField(
        'Аватар', upload_to='profiles/', blank=True
    )
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
