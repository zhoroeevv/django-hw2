# Generated by Django 5.0.3 on 2024-03-30 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('image', models.ImageField(upload_to='info_user/', verbose_name='Фотография пользователя')),
            ],
            options={
                'verbose_name': 'Данные пользователя',
                'verbose_name_plural': 'Данные пользователей',
            },
        ),
        migrations.DeleteModel(
            name='Geeks',
        ),
    ]
