from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    ordering = ["email"]
    model = User
    list_display = [
        "email",
        "is_superuser",
    ]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('ФИО', {'fields': ('name',
                            'surname',
                            'last_name',
                            )}), (
            'Остальные данные',
            {
                'fields': (
                    'sex',
                    'date_of_birth',
                    'citizenship',
                    'region',
                    'phone',
                    'image_profile',
                ),
            },
        ),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),

    )


admin.site.register(User, CustomUserAdmin)
