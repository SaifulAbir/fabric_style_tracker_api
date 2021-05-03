# Generated by Django 3.2 on 2021-05-03 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FabricConstruction',
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
                ('ends_per_inch', models.PositiveIntegerField(unique=True)),
                ('picks_per_inch', models.PositiveIntegerField(unique=True)),
                ('warp_count', models.PositiveIntegerField(unique=True)),
                ('weft_count', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Fabric Construction',
                'verbose_name_plural': 'Fabric Constructions',
                'db_table': 'fabric_constructions',
            },
        ),
        migrations.CreateModel(
            name='FabricType',
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
                'verbose_name': 'Fabric Type',
                'verbose_name_plural': 'Fabric Types',
                'db_table': 'fabric_types',
            },
        ),
        migrations.CreateModel(
            name='Fiber',
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
                'verbose_name': 'Fiber',
                'verbose_name_plural': 'Fibers',
                'db_table': 'fibers',
            },
        ),
        migrations.CreateModel(
            name='Shrinkage',
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
                ('wrap', models.PositiveIntegerField()),
                ('weft', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Shrinkage',
                'verbose_name_plural': 'Shrinkage',
                'db_table': 'shrinkage',
            },
        ),
        migrations.CreateModel(
            name='FabricComposition',
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
                ('percentage', models.PositiveIntegerField()),
                ('fiber', models.ForeignKey(db_column='fiber', on_delete=django.db.models.deletion.PROTECT, to='fabric.fiber')),
            ],
            options={
                'verbose_name': 'Fabric Composition',
                'verbose_name_plural': 'Fabric Compositions',
                'db_table': 'fabric_compositions',
            },
        ),
        migrations.CreateModel(
            name='Fabric',
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
                ('dekko_reference', models.CharField(max_length=255, unique=True)),
                ('mill_reference', models.CharField(max_length=255, unique=True)),
                ('weight', models.PositiveIntegerField(blank=True, null=True)),
                ('cuttable_width', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('moq', models.PositiveIntegerField(blank=True, null=True)),
                ('lead_time', models.PositiveIntegerField(blank=True, null=True)),
                ('availability', models.PositiveIntegerField(blank=True, null=True)),
                ('marketing_tools', models.TextField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('composition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fabric.fabriccomposition')),
                ('construction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fabric.fabricconstruction')),
                ('fabric_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fabric.fabrictype')),
                ('shrinkage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fabric.shrinkage')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplier.supplier')),
            ],
            options={
                'verbose_name': 'Fabric',
                'verbose_name_plural': 'Fabrics',
                'db_table': 'fabrics',
            },
        ),
    ]
