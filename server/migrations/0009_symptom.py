# Generated by Django 2.0.2 on 2018-03-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_account_archive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
