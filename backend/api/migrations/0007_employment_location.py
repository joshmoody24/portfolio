# Generated by Django 4.1.2 on 2022-11-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_employment_end_date_employment_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employment',
            name='location',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
