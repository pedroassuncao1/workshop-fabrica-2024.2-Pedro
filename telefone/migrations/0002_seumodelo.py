# Generated by Django 5.1 on 2024-08-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telefone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeuModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.CharField(max_length=100)),
                ('campo2', models.IntegerField()),
                ('campo3', models.DateTimeField()),
            ],
        ),
    ]
