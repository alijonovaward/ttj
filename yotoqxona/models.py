from django.db import models


class Dormitory(models.Model):
    director = models.ForeignKey("accounts.Director", on_delete=models.PROTECT, related_name='dormitories')
    name = models.CharField(max_length=300, blank=False)
    address = models.CharField(max_length=300, blank=False)
    monthly_payment = models.PositiveIntegerField(default=0, verbose_name="Oylik to‘lov miqdori (so'm)")
    default_monthly_payment = models.PositiveIntegerField(
        default=1,
        help_text="Shartnomaga asosan boshlang‘ich oylik to‘lov (so‘mda)"
    )
    def __str__(self):
        return self.name

class Device(models.Model):
    dormitory = models.ForeignKey(Dormitory, on_delete=models.PROTECT, related_name='devices')
    ipaddress = models.CharField(max_length=25, blank=False)
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    entrance = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk} -> {self.dormitory.name} -> {self.entrance}"

class Room(models.Model):
    dormitory = models.ForeignKey(Dormitory, on_delete=models.PROTECT, related_name='rooms')
    number = models.CharField(max_length=15)
    size = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('dormitory', 'number')  # Har bir yotoqxona ichida unique
        verbose_name = "Xona"
        verbose_name_plural = "Xonalar"

    def __str__(self):
        return f"{self.dormitory.name} - {self.number}"

