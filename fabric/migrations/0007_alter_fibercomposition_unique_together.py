# Generated by Django 3.2.3 on 2021-06-15 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabric', '0006_auto_20210529_0437'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fibercomposition',
            unique_together={('fiber_percentage', 'fabric_composition')},
        ),
    ]
