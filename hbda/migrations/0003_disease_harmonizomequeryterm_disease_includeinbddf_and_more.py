# Generated by Django 4.1 on 2023-01-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hbda', '0002_remove_disease_diseaseslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='HarmonizomeQueryTerm',
            field=models.CharField(default='', help_text='Name of Disease for Harmonizome', max_length=500, null=True, verbose_name='Disease Name for Harmonizome'),
        ),
        migrations.AddField(
            model_name='disease',
            name='includeInBDDF',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='disease',
            name='numGeneHarmonizome',
            field=models.PositiveIntegerField(help_text='Number of Genes (Harmonizome)', null=True, verbose_name='No. of Genes (Harmonizome)'),
        ),
    ]
