# Generated by Django 2.0.2 on 2018-03-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_auto_20180306_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='speciality',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]