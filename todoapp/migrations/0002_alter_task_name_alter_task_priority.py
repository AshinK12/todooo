# Generated by Django 4.2.3 on 2023-07-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(max_length=50),
        ),
    ]
