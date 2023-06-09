# Generated by Django 4.1.7 on 2023-04-01 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.IntegerField()),
                ('messageId', models.CharField(max_length=200)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('network_code', models.CharField(blank=True, max_length=100, null=True)),
                ('failure_reason', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
