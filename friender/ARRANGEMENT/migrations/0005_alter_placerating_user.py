# Generated by Django 4.2 on 2023-04-25 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ARRANGEMENT', '0004_remove_places_arrangement_arrangements_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placerating',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ARRANGEMENT.users'),
        ),
    ]
