# Generated by Django 3.2.10 on 2021-12-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dec', models.TextField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
