# Generated by Django 4.1 on 2022-12-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdpm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meningioma_3_PXD012923',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proteinId', models.CharField(default='', help_text='UniProt Protein ID', max_length=200, verbose_name='Protein ID')),
                ('S1', models.FloatField()),
                ('S2', models.FloatField()),
                ('S3', models.FloatField()),
                ('S4', models.FloatField()),
                ('S5', models.FloatField()),
                ('S6', models.FloatField()),
                ('S7', models.FloatField()),
                ('S8', models.FloatField()),
                ('S9', models.FloatField()),
                ('S10', models.FloatField()),
                ('S11', models.FloatField()),
                ('S12', models.FloatField()),
                ('S13', models.FloatField()),
                ('S14', models.FloatField()),
                ('S15', models.FloatField()),
                ('S16', models.FloatField()),
                ('S17', models.FloatField()),
                ('S18', models.FloatField()),
                ('S19', models.FloatField()),
                ('S20', models.FloatField()),
                ('S21', models.FloatField()),
                ('S22', models.FloatField()),
                ('S23', models.FloatField()),
                ('S24', models.FloatField()),
                ('S25', models.FloatField()),
                ('S26', models.FloatField()),
                ('S27', models.FloatField()),
                ('S28', models.FloatField()),
                ('S29', models.FloatField()),
                ('S30', models.FloatField()),
                ('S31', models.FloatField()),
                ('S32', models.FloatField()),
                ('S33', models.FloatField()),
                ('S34', models.FloatField()),
                ('S35', models.FloatField()),
                ('S36', models.FloatField()),
                ('S37', models.FloatField()),
                ('S38', models.FloatField()),
                ('S39', models.FloatField()),
                ('S40', models.FloatField()),
                ('S41', models.FloatField()),
                ('S42', models.FloatField()),
                ('S43', models.FloatField()),
                ('S44', models.FloatField()),
                ('S45', models.FloatField()),
                ('S46', models.FloatField()),
                ('S47', models.FloatField()),
                ('S48', models.FloatField()),
                ('S49', models.FloatField()),
                ('S50', models.FloatField()),
                ('S51', models.FloatField()),
                ('S52', models.FloatField()),
                ('S53', models.FloatField()),
                ('S54', models.FloatField()),
                ('S55', models.FloatField()),
                ('S56', models.FloatField()),
                ('S57', models.FloatField()),
                ('S58', models.FloatField()),
                ('S59', models.FloatField()),
                ('S60', models.FloatField()),
                ('S61', models.FloatField()),
                ('S62', models.FloatField()),
                ('S63', models.FloatField()),
                ('S64', models.FloatField()),
                ('S65', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Meningioma_3_PXD012923_Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceName', models.TextField(help_text='Name of Source File', verbose_name='Source Name')),
                ('sampleId', models.CharField(help_text='The Sample ID', max_length=50, verbose_name='Sample ID')),
                ('sampleName', models.TextField(help_text='Name of Sample', verbose_name='Sample Name')),
                ('gender', models.IntegerField(choices=[('0', 'Male'), ('1', 'Female')], null=True)),
                ('age', models.IntegerField(help_text='Age of Patient', null=True, verbose_name='Age')),
                ('groupI', models.IntegerField(choices=[('0', 'Control'), ('1', 'Disease')], null=True)),
                ('groupII', models.IntegerField(choices=[(0, 'Control'), (1, 'Grade I'), (2, 'Grade II'), (3, 'Grade III')], null=True)),
                ('groupIII', models.IntegerField(choices=[(0, 'Skull Base'), (1, 'Convexity'), (2, 'Other')], null=True)),
                ('groupIV', models.IntegerField(choices=[(0, 'Primary'), (1, 'Recurrence 1st'), (2, 'Recurrence 2nd')], null=True)),
            ],
        ),
    ]
