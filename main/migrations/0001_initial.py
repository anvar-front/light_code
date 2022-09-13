# Generated by Django 4.1.1 on 2022-09-11 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование станка')),
            ],
            options={
                'verbose_name': 'Станок',
                'verbose_name_plural': 'Станки',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Начало')),
                ('end_time', models.DateTimeField(verbose_name='Конец')),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee', verbose_name='Сотрудник')),
                ('machine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.machine', verbose_name='Станок')),
            ],
            options={
                'verbose_name': 'Рабочее время',
                'verbose_name_plural': 'Рабочее время',
            },
        ),
    ]