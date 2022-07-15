from pyexpat import model
from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import User


class Administrateur(models.Model):
    AU_id = models.OneToOneField(User, on_delete=models.CASCADE)
    adm_lastname = models.CharField(max_length=15)
    adm_firstname = models.CharField(max_length=15)
    adm_tel = models.IntegerField()
    adm_isadmin = models.BooleanField(default=True)


class Medicament(models.Model):
    mdc_name = models.CharField(max_length=20)
    mdc_price = models.FloatField(default=10.00)
    mdc_dateexp = models.DateField()
    mdc_fournisseur = models.CharField(max_length=15)
    mdc_qts = models.IntegerField(default=1)


class Clients(models.Model):
    CU_id = models.OneToOneField(User, on_delete=models.CASCADE)
    clt_lastname = models.CharField(max_length=15)
    clt_firstname = models.CharField(max_length=15)
    clt_tel = models.CharField(max_length=20)
    clt_city = models.CharField(max_length=25, default='casablanca')
    clt_zip = models.CharField(max_length=10, default=20000)
    clt_adresse = models.CharField(max_length=300)


class Commande(models.Model):
    cmd_montant = models.FloatField()
    cmd_datecmd = models.DateField()
    clt_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    adm_id = models.ForeignKey(Administrateur, on_delete=models.CASCADE)


class Order(models.Model):
    cmd_id = models.ForeignKey(Commande, on_delete=models.CASCADE)
    mdc_id = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    order_qts = models.IntegerField()
    order_prix = models.FloatField()
