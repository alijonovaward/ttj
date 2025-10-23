from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('director', 'Direktor'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='other',
        verbose_name='Lavozim'
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Telefon raqami'
    )



class Director(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def clean(self):
        if self.user.role != 'director':
            raise ValidationError("Faqat direktor roliga ega foydalanuvchini bog'lashingiz mumkin.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.get_full_name()} (Direktor)"

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='admin')

    def __str__(self):
        return f"Admin -> {self.user.get_full_name()}"
