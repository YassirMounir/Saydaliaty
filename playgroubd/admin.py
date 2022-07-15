from django.contrib import admin
from .models import Administrateur, Clients, Commande, Medicament, Order

# Register your models here.
admin.site.register(Clients),
admin.site.register(Administrateur),
admin.site.register(Medicament),
admin.site.register(Commande),
admin.site.register(Order),