from django.contrib import admin
from .models import InvestmentModel
from django.contrib.auth.models import User
# Register your models here.


admin.site.register(InvestmentModel)

User.objects.filter(email='admin@gmail.com').delete()
User.objects.create_superuser('admin', 'admin@gmail.com', 'password')