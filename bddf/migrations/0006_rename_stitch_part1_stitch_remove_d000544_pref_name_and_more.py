# Generated by Django 4.1.3 on 2023-05-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bddf', '0005_d000544_pref_name_d000690_pref_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stitch_Part1',
            new_name='Stitch',
        ),
        migrations.RemoveField(
            model_name='d000544',
            name='pref_name',
        ),
        migrations.RemoveField(
            model_name='d000690',
            name='pref_name',
        ),
        migrations.RemoveField(
            model_name='d005909',
            name='pref_name',
        ),
        migrations.RemoveField(
            model_name='d005910',
            name='pref_name',
        ),
        migrations.RemoveField(
            model_name='d006816',
            name='pref_name',
        ),
        migrations.RemoveField(
            model_name='d008527',
            name='pref_name',
        ),
        migrations.RemoveField(
            model_name='d008579',
            name='pref_name',
        ),
        migrations.RemoveField(
            model_name='d009103',
            name='pref_name',
        ),
        migrations.RemoveField(
            model_name='d010300',
            name='pref_name',
        ),
        migrations.RemoveField(
            model_name='d049912',
            name='pref_name',
        ),
        migrations.RemoveField(
            model_name='d057174',
            name='pref_name',
        ),
        migrations.AlterField(
            model_name='d000544',
            name='Drug_Name',
            field=models.CharField(default='', help_text='Drug Name', max_length=2000, verbose_name='Drug Name'),
        ),
        migrations.AlterField(
            model_name='d000690',
            name='Drug_Name',
            field=models.CharField(default='', help_text='Drug Name', max_length=2000, verbose_name='Drug Name'),
        ),
        migrations.AlterField(
            model_name='d005909',
            name='Drug_Name',
            field=models.CharField(default='', help_text='Drug Name', max_length=2000, verbose_name='Drug Name'),
        ),
        migrations.AlterField(
            model_name='d005910',
            name='Drug_Name',
            field=models.CharField(default='', help_text='Drug Name', max_length=2000, verbose_name='Drug Name'),
        ),
        migrations.AlterField(
            model_name='d006816',
            name='Drug_Name',
            field=models.CharField(default='', help_text='Drug Name', max_length=2000, verbose_name='Drug Name'),
        ),
        migrations.AlterField(
            model_name='d008527',
            name='Drug_Name',
            field=models.CharField(default='', help_text='Drug Name', max_length=2000, verbose_name='Drug Name'),
        ),
        migrations.AlterField(
            model_name='d008579',
            name='Drug_Name',
            field=models.CharField(default='', help_text='Drug Name', max_length=2000, verbose_name='Drug Name'),
        ),
        migrations.AlterField(
            model_name='d009103',
            name='Drug_Name',
            field=models.CharField(default='', help_text='Drug Name', max_length=2000, verbose_name='Drug Name'),
        ),
        migrations.AlterField(
            model_name='d010300',
            name='Drug_Name',
            field=models.CharField(default='', help_text='Drug Name', max_length=2000, verbose_name='Drug Name'),
        ),
        migrations.AlterField(
            model_name='d049912',
            name='Drug_Name',
            field=models.CharField(default='', help_text='Drug Name', max_length=2000, verbose_name='Drug Name'),
        ),
        migrations.AlterField(
            model_name='d057174',
            name='Drug_Name',
            field=models.CharField(default='', help_text='Drug Name', max_length=2000, verbose_name='Drug Name'),
        ),
    ]
