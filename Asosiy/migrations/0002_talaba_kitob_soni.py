# Generated by Django 5.0.1 on 2024-01-16 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talaba',
            name='kitob_soni',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
