# Generated by Django 2.2 on 2019-08-09 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликована ли машина'),
        ),
    ]
