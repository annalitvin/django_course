from django.db import models
from PIL import Image

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=80, verbose_name="Фамилия")


class Teacher(Person, models.Model):
    photo = models.ImageField(upload_to="image_photo")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    employment = models.DateField(verbose_name="Дата приема на работу")
    salary = models.FloatField()

class Class(models.Model):
    number = models.PositiveIntegerField(verbose_name='Номер класса')
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Учитель")


class Student(Person, models.Model):
    age = models.DateField()
    phone = models.CharField(max_length=10, verbose_name="Телефон")
    email = models.EmailField(max_length=254, verbose_name="E-mail")
    clas = models.ForeignKey(Class, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Класс")