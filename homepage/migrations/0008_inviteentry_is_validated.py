# Generated by Django 3.0.4 on 2020-05-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_inviteentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='inviteentry',
            name='is_validated',
            field=models.BooleanField(default=False),
        ),
    ]
