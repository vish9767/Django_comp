# Generated by Django 3.2.10 on 2021-12-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('dec', models.TextField(max_length=200)),
                ('price', models.IntegerField(max_length=4)),
                ('pic', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.AlterField(
            model_name='slid',
            name='dec',
            field=models.TextField(max_length=200),
        ),
    ]
