from django.db import models

# Create your models here.
class Categoria(models.Model):
  idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
  nombreCategoria = models.CharField(max_length=50, verbose_name ="Nombre de la categoria")

  def __str__(self):
    return self.nombreCategoria

class Libro(models.Model):
  Isbn = models.IntegerField(primary_key=True, verbose_name='Isbn Del Libro')
  nombre = models.CharField(max_length=50, verbose_name ="Nombre del Libro")
  autor= models.CharField(max_length=50, verbose_name ="Autor")
  descripcion = models.CharField(max_length=200, verbose_name ="Descripción")
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

  def __int__(self):
    return self.Isbn

