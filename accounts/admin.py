from django.contrib import admin
from .models import CustomUser, Director, Employee

admin.site.register(CustomUser)
admin.site.register(Director)
admin.site.register(Employee)