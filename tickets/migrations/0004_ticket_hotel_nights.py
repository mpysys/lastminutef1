# Generated by Django 4.1.4 on 2022-12-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_category_options_ticket_countryimg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='hotel_nights',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
