# Generated by Django 4.1.4 on 2022-12-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_rename_has_length_ticket_has_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='dates',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
