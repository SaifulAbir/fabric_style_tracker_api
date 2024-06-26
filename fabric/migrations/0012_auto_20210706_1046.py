# Generated by Django 3.2.3 on 2021-07-06 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fabric', '0011_auto_20210705_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('created_from', models.CharField(max_length=255, null=True)),
                ('modified_by', models.CharField(max_length=255, null=True)),
                ('modified_at', models.DateTimeField(null=True)),
                ('modified_from', models.CharField(max_length=255, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('archived_by', models.CharField(max_length=255, null=True)),
                ('archived_at', models.DateTimeField(null=True)),
                ('archived_from', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Appearance',
                'verbose_name_plural': 'Appearances',
                'db_table': 'appearances',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Weave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('created_from', models.CharField(max_length=255, null=True)),
                ('modified_by', models.CharField(max_length=255, null=True)),
                ('modified_at', models.DateTimeField(null=True)),
                ('modified_from', models.CharField(max_length=255, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('archived_by', models.CharField(max_length=255, null=True)),
                ('archived_at', models.DateTimeField(null=True)),
                ('archived_from', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Weave',
                'verbose_name_plural': 'Weaves',
                'db_table': 'weaves',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='fabric',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='fabric',
            name='appearance',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='fabric.appearance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fabric',
            name='weave',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='fabric.weave'),
            preserve_default=False,
        ),
    ]
