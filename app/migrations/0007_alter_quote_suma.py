# Generated by Django 4.0.4 on 2022-06-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_quote_suma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='suma',
            field=models.IntegerField(default=0),
        ),
    ]