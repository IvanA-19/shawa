# Generated by Django 5.1.2 on 2024-11-05 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название ингредиента')),
                ('ingredient_weight', models.FloatField(blank=True, null=True, verbose_name='Вес ингредиента')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Shawarma_points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Адрес ресторана')),
            ],
            options={
                'verbose_name': 'Точка продаж шаурмы',
                'verbose_name_plural': 'Точки продаж шаурмы',
            },
        ),
        migrations.CreateModel(
            name='Shawarmas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shawarma_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название шаурмы')),
                ('shawarma_ingredients', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ингредиенты шаурмы')),
                ('shawarma_price', models.FloatField(blank=True, null=True, verbose_name='Цена шаурмы')),
            ],
            options={
                'verbose_name': 'Шаурма',
                'verbose_name_plural': 'Шаурмы',
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя работника')),
                ('worker_last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия работника')),
                ('worker_middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество работника')),
                ('worker_position', models.IntegerField(blank=True, null=True, verbose_name='Должность работника')),
                ('worker_point_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shawarma_points', verbose_name='ID ресторана')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='ingredient_point_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shawarma_points', verbose_name='ID ресторана'),
        ),
    ]
