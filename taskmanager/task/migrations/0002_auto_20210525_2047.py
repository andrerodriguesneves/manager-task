# Generated by Django 3.2.3 on 2021-05-25 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='task',
            name='solution',
            field=models.TextField(blank=True, max_length=500, verbose_name='Solução'),
        ),
    ]
