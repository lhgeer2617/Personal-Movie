# Generated by Django 4.2.4 on 2023-11-24 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('여성', '여성'), ('남성', '남성')], default='남성', max_length=10),
        ),
    ]
