# Generated by Django 3.1.5 on 2021-02-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20210128_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='description',
        ),
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(choices=[('green', 'Зеленый'), ('orange', 'Оранжевый'), ('purple', 'Фиолетовый')], default='green', max_length=6, unique=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(choices=[('green', 'Завтрак'), ('orange', 'Обед'), ('purple', 'Ужин')], default='orange', max_length=10, unique=True, verbose_name='Название'),
        ),
    ]
