# Generated by Django 4.1 on 2022-10-10 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseTrait',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('pubmedid', models.IntegerField(primary_key=True, serialize=False)),
                ('journal', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('link', models.CharField(default=None, max_length=200)),
            ],
            options={
                'ordering': ['pubmedid'],
            },
        ),
        migrations.CreateModel(
            name='Snp',
            fields=[
                ('rsid', models.IntegerField(primary_key=True, serialize=False)),
                ('chrom', models.CharField(max_length=50)),
                ('chrom_pos', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['rsid'],
            },
        ),
        migrations.CreateModel(
            name='Snp2Phenotype2Ref',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pvalue', models.FloatField()),
                ('neg_log10_pvalue', models.FloatField()),
                ('comment', models.CharField(default=None, max_length=200)),
                ('disease_trait_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snpsdiseasesapp.diseasetrait')),
                ('reference_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snpsdiseasesapp.reference')),
                ('snp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snpsdiseasesapp.snp')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]