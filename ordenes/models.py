from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Client(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Nombre")
    address = models.CharField(max_length = 100, verbose_name = "Direccion")
    email = models.EmailField(max_length = 50, verbose_name = "Correo")

    date = models.DateTimeField(default = now, verbose_name = "Fecha Creacion")

    class Meta():
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Nombre Categoria")

    date = models.DateTimeField(default = now, verbose_name = "Fecha Creacion")

    class Meta():
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    def __str__(self): return self.name

class Ot(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Nombre OT")
    detail = models.TextField(verbose_name = "Detalle")

    owner = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Responsable")
    clt = models.ForeignKey(Client, on_delete = models.CASCADE, verbose_name = "Asignada")
    ctg = models.ManyToManyField(Category, verbose_name = "Categorias")

    dateOt = models.DateTimeField(default = now, verbose_name = "Fecha Creacion")

    class Meta():
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"
    def __str__(self): return self.name