# Generated by Django 4.2.1 on 2023-05-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0022_alter_appointment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='google_meet_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
