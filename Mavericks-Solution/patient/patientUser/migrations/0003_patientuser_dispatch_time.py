# Generated by Django 4.1.7 on 2023-04-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientUser', '0002_alter_patientuser_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientuser',
            name='dispatch_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
