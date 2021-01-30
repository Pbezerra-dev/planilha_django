# Generated by Django 3.1.3 on 2020-12-29 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_spent_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='spent',
            name='number_plots',
            field=models.IntegerField(default=2, verbose_name='Numero de parcelas'),
        ),
        migrations.AddField(
            model_name='spent',
            name='parceled_out',
            field=models.BooleanField(default=False, verbose_name='Parcelada'),
        ),
    ]
