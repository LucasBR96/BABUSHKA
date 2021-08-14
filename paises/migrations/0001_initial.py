# Generated by Django 3.2.4 on 2021-08-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=30, unique=True)),
                ('slug', models.SlugField(max_length=30)),
            ],
            options={
                'db_table': 'pais',
                'ordering': ('nome',),
            },
        ),
    ]
