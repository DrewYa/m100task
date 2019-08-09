from django.db import models


class Car(models.Model):
    name = models.CharField('Название', max_length=50)
    reg_number = models.CharField('Регистрационный номер машины', max_length=50, unique=True)
    is_published = models.BooleanField('Опубликована ли машина', default=True)
