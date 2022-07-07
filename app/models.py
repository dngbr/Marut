from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    nume = models.CharField(max_length=30)
    profil = models.CharField(max_length=30)
    deschidere = models.CharField(max_length=30)
    lungime = models.IntegerField()
    inaltime = models.IntegerField()
    culoare = models.CharField(max_length=20)
    sticla = models.CharField(max_length=20)
    pret = models.IntegerField()
    imagine = models.CharField(max_length=30)

    def __str__(self) -> str:
        return str(self.id)+' '+str(self.nume)+' '+str(self.profil)+' '+str(self.deschidere)+' '+str(self.lungime)+'x'+str(self.inaltime)+' '+str(self.culoare)+' '+str(self.sticla)+' '+str(self.pret)


class Quote(models.Model):
    nume = models.CharField(max_length=30)
    prenume = models.CharField(max_length=30)
    email = models.EmailField()
    telefon = models.CharField(max_length=30)
    adresa = models.CharField(max_length=30)
    suma = models.IntegerField(default=0)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return "Comanda nr "+str(self.id)+" - " + self.nume + " " + self.prenume + " | " + self.telefon + " | " + str(self.email)


class Product_in_Quote(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.nume) + ' ' + str(self.product.profil)+' ' + str(self.product.lungime) + "x" + str(self.product.inaltime) + ' ' + self.product.deschidere + ' ' + self.product.culoare + ' ' + self.product.sticla


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nume = models.CharField(max_length=30, blank=True, null=True)
    prenume = models.CharField(max_length=30, blank=True, null=True)
    telefon = models.CharField(max_length=30, blank=True, null=True)
    adresa = models.CharField(max_length=30, blank=True, null=True)
    data_created = models.DateTimeField(
        auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)
