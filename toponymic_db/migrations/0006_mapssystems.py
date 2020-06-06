# Generated by Django 3.0.7 on 2020-06-06 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toponymic_db', '0005_geosystems'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapsSystems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_system_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='toponymic_db.GeoSystems')),
                ('map_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='toponymic_db.Maps')),
            ],
        ),
    ]