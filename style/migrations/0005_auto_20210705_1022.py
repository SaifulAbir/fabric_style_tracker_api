# Generated by Django 3.2.3 on 2021-07-05 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0004_auto_20210703_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='designer',
            options={'ordering': ['-created_at'], 'verbose_name': 'Designer', 'verbose_name_plural': 'Designers'},
        ),
        migrations.AlterModelOptions(
            name='style',
            options={'ordering': ['-created_at'], 'verbose_name': 'Style', 'verbose_name_plural': 'Styles'},
        ),
        migrations.AlterModelOptions(
            name='washtype',
            options={'ordering': ['-created_at'], 'verbose_name': 'Wash Type', 'verbose_name_plural': 'Wash Types'},
        ),
    ]
