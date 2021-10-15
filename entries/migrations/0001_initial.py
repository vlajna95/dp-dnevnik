# Generated by Django 3.2.8 on 2021-10-12 06:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Naslov')),
                ('content', models.TextField(verbose_name='Sadržaj unosa')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Unos',
                'verbose_name_plural': 'Unosi',
            },
        ),
    ]
