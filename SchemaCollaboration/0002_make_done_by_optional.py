# Generated by Django 3.1.1 on 2020-09-08 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200908_1130'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name_plural': 'TO DOs'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='done_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='done_by_author', to='core.person'),
        ),
    ]
