# Generated by Django 4.2.1 on 2023-05-31 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0027_diagnosticorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosticorder',
            name='patient_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
