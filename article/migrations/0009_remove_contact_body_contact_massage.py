# Generated by Django 4.2.3 on 2023-08-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_contact_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='body',
        ),
        migrations.AddField(
            model_name='contact',
            name='Massage',
            field=models.TextField(null=True),
        ),
    ]
