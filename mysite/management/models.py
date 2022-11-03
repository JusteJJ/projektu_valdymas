from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projektas(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=200)
    pradziosdata = models.DateField("Pradžios data", max_length=100)
    pabaigosdata = models.DateField("Pabaigos data", max_length=100)
    vadovas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    klientas1 = models.CharField("Klientas", max_length=100)
    darbuotojai = models.CharField("Darbuotojai", max_length=100)
    darbai = models.CharField("Darbai", max_length=200)
    saskaitos = models.CharField("Sąskaitos", max_length=100)

    STATUS = (
        ("v", "Vykdomas"),
        ("b", "Baigtas vykdyti")
    )

    statusas = models.CharField(max_length=1, choices=STATUS, default="v", help_text="Statusas")
    def __str__(self):
        return f"{self.pavadinimas}"
    class Meta:
        verbose_name = "Projektas"
        verbose_name_plural = "Projektai"

#"****************************************************"
class Klientas(models.Model):
    klientas1 = models.ForeignKey("Projektas", on_delete=models.SET_NULL, null=True)
    vardaspavarde = models.CharField("Vardas Pavardė", max_length=100)
    imone = models.CharField("Įmonė", max_length=100)
    kontaktai = models.CharField("Kontaktai", max_length=100)

    def __str__(self):
        return f"{self.vardaspavarde} ({self.imone}, {self.kontaktai})"
    class Meta:
        verbose_name = "Klientas"
        verbose_name_plural = "Klientai"

#"****************************************************"
class Darbuotojas(models.Model):
    darbuotojai = models.ForeignKey("Projektas", on_delete=models.SET_NULL, null=True)
    vardaspavarde2 = models.CharField("Vardas Pavardė", max_length=100)
    pareigos = models.CharField("Pareigos", max_length=100)

    def __str__(self):
        return f"{self.vardaspavarde2} ({self.pareigos})"
    class Meta:
        verbose_name = "Darbuotojas"
        verbose_name_plural = "Darbuotojai"

#"****************************************************"
class Darbas(models.Model):
    darbai = models.ForeignKey("Projektas", on_delete=models.SET_NULL, null=True)
    pavadinimas2 = models.CharField("Pavadinimas", max_length=100)
    pastabos = models.CharField("Pastabos", max_length=100)

    def __str__(self):
        return f"{self.pavadinimas2} ({self.pastabos})"
    class Meta:
        verbose_name = "Darbas"
        verbose_name_plural = "Ateityje vykdomi darbai"

#"****************************************************"
class Saskaita(models.Model):
    saskaitos = models.ForeignKey("Projektas", on_delete=models.SET_NULL, null=True)
    data = models.DateField("Išrašymo data")
    suma = models.FloatField("Suma", max_length=100)

    def __str__(self):
        return f"{self.data} {self.suma}"
    class Meta:
        verbose_name = "Sąskaita"
        verbose_name_plural = "Sąskaitos"