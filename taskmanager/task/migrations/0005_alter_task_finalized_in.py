# Generated by Django 3.2.3 on 2021-05-25 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20210525_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finalized_in',
            field=models.DateTimeField(null=True, verbose_name='Finalizado em'),
        ),
    ]
