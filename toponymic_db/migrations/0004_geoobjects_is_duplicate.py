# Generated by Django 3.0.7 on 2020-06-06 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toponymic_db', '0003_auto_20200606_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoobjects',
            name='is_duplicate',
            field=models.IntegerField(null=True),
        ),
    ]
