# Generated by Django 3.1.2 on 2020-10-13 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_makes_behaviour_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapackage',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.datapackagestatus'),
        ),
    ]
