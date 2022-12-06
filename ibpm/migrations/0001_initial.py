# Generated by Django 4.1 on 2022-11-25 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneProt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protName', models.CharField(help_text='The Protein Name', max_length=100, unique=True, verbose_name='Protein Name')),
                ('entryName', models.CharField(help_text='The UniProt Entry Name Corresponding to this Protein', max_length=100, verbose_name='UniProt Entry Name')),
                ('geneName', models.CharField(blank=True, default='', help_text='Abbrievated Name of the Gene', max_length=200, verbose_name='Gene Name')),
                ('altGeneNames', models.TextField(blank=True, help_text='A (demarcated) string containing all the possible gene names', verbose_name='Alternate Gene Names')),
                ('geneProtFullNames', models.TextField(help_text='A (demarcated) string containing all the possible full gene names', verbose_name='Gene Full Names')),
                ('chromosome', models.CharField(choices=[('0', 'Unplaced'), ('1', 'Chromosome 1'), ('2', 'Chromosome 2'), ('3', 'Chromosome 3'), ('4', 'Chromosome 4'), ('5', 'Chromosome 5'), ('6', 'Chromosome 6'), ('7', 'Chromosome 7'), ('8', 'Chromosome 8'), ('9', 'Chromosome 9'), ('10', 'Chromosome 10'), ('11', 'Chromosome 11'), ('12', 'Chromosome 12'), ('13', 'Chromosome 13'), ('14', 'Chromosome 14'), ('15', 'Chromosome 15'), ('16', 'Chromosome 16'), ('17', 'Chromosome 17'), ('18', 'Chromosome 18'), ('19', 'Chromosome 19'), ('20', 'Chromosome 20'), ('21', 'Chromosome 21'), ('22', 'Chromosome 22'), ('X', 'Chromosome X'), ('Y', 'Chromosome Y'), ('M', 'Mitochondrion'), ('NA', 'Not Applicable')], default=0, max_length=2)),
                ('protLength', models.PositiveIntegerField(help_text='Length of Protein (AA)', null=True, verbose_name='Protein Length')),
                ('protMass', models.PositiveIntegerField(help_text='Mass of Protein (in kDa)', null=True, verbose_name='Protein Mass')),
            ],
        ),
        migrations.CreateModel(
            name='Protein',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proteinId', models.CharField(help_text='The Protein Name', max_length=100, verbose_name='Protein Name')),
                ('AMY_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Amygdala', verbose_name='Amygdala - LH')),
                ('AMY_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Amygdala', verbose_name='Amygdala - RH')),
                ('AMY_Med', models.FloatField(default=0, help_text='Median Intensity - Amygdala', verbose_name='Amygdala - Median')),
                ('BS_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Brain Stem', verbose_name='Brain Stem - LH')),
                ('BS_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Brain Stem', verbose_name='Brain Stem - Median')),
                ('BS_Med', models.FloatField(default=0, help_text='Median Intensity - Brain Stem', verbose_name='Brain Stem - RH')),
                ('CING_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Cingulum', verbose_name='Cingulum - LH')),
                ('CING_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Cingulum', verbose_name='Cingulum - RH')),
                ('CING_Med', models.FloatField(default=0, help_text='Median Intensity - Cingulum', verbose_name='Cingulum - Median')),
                ('CN_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Caudate Nucelus', verbose_name='Caudate Nucelus - LH')),
                ('CN_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Caudate Nucelus', verbose_name='Caudate Nucelus - RH')),
                ('CN_Med', models.FloatField(default=0, help_text='Median Intensity - Caudate Nucelus', verbose_name='Caudate Nucelus - Median')),
                ('CV_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Cerbellar Vermis', verbose_name='Cerbellar Vermis - LH')),
                ('CV_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Cerbellar Vermis', verbose_name='Cerbellar Vermis - RH')),
                ('CV_Med', models.FloatField(default=0, help_text='Median Intensity - Cerbellar Vermis', verbose_name='Cerbellar Vermis - Median')),
                ('DG_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Dentate Gyrus', verbose_name='Dentate Gyrus - LH')),
                ('DG_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Dentate Gyrus', verbose_name='Dentate Gyrus - RH')),
                ('DG_Med', models.FloatField(default=0, help_text='Median Intensity - Dentate Gyrus', verbose_name='Dentate Gyrus - Median')),
                ('FCM_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Frontal Cortex Media ', verbose_name='Frontal Cortex Media - LH')),
                ('FCM_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Frontal Cortex Media', verbose_name='Frontal Cortex Media - RH')),
                ('FCM_Med', models.FloatField(default=0, help_text='Median Intensity - Frontal Cortex Media', verbose_name='Frontal Cortex Media - Median')),
                ('FWM_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Frontal White Matter', verbose_name='Frontal White Matter - LH')),
                ('FWM_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Frontal White Matter', verbose_name='Frontal White Matter - RH')),
                ('FWM_Med', models.FloatField(default=0, help_text='Median Intensity - Frontal White Matter', verbose_name='Frontal White Matter - Median')),
                ('HIP_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Hippocampus', verbose_name='Hippocampus - LH')),
                ('HIP_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Hippocampus', verbose_name='Hippocampus - RH')),
                ('HIP_Med', models.FloatField(default=0, help_text='Median Intensity - Hippocampus', verbose_name='Hippocampus - Median')),
                ('LE_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Lentiform Extern', verbose_name='Lentiform Extern - LH')),
                ('LE_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Lentiform Extern', verbose_name='Lentiform Extern - RH')),
                ('LE_Med', models.FloatField(default=0, help_text='Median Intensity - Lentiform Extern', verbose_name='Lentiform Extern - Median')),
                ('LI_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Lentiform Intern', verbose_name='Lentiform Intern - LH')),
                ('LI_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Lentiform Intern', verbose_name='Lentiform Intern - RH')),
                ('LI_Med', models.FloatField(default=0, help_text='Median Intensity - Lentiform Intern', verbose_name='Lentiform Intern - Median')),
                ('OB_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Olfactory Bulb', verbose_name='Olfactory Bulb - LH')),
                ('OB_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Olfactory Bulb', verbose_name='Olfactory Bulb - RH')),
                ('OB_Med', models.FloatField(default=0, help_text='Median Intensity - Olfactory Bulb', verbose_name='Olfactory Bulb - Median')),
                ('OC_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Occipital Cortex', verbose_name='Occipital Cortex - LH')),
                ('OC_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Occipital Cortex', verbose_name='Occipital Cortex - RH')),
                ('OC_Med', models.FloatField(default=0, help_text='Median Intensity - Occipital Cortex', verbose_name='Occipital Cortex - Median')),
                ('PC_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Parietal Cortex', verbose_name='Parietal Cortex - LH')),
                ('PC_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - ', verbose_name='Parietal Cortex - RH')),
                ('PC_Med', models.FloatField(default=0, help_text='Median Intensity - Parietal Cortex', verbose_name='Parietal Cortex - Median')),
                ('PONS_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Pons', verbose_name='Pons - LH')),
                ('PONS_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Pons', verbose_name='Pons - RH')),
                ('PONS_Med', models.FloatField(default=0, help_text='Median Intensity - Pons', verbose_name='Pons - Median')),
                ('PUT_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Putamen', verbose_name='Putamen - LH')),
                ('PUT_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Putamen', verbose_name='Putamen - RH')),
                ('PUT_Med', models.FloatField(default=0, help_text='Median Intensity - Putamen', verbose_name='Putamen - Median')),
                ('SN_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Substantia Nigra', verbose_name='Substantia Nigra - LH')),
                ('SN_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Substantia Nigra', verbose_name='Substantia Nigra - RH')),
                ('SN_Med', models.FloatField(default=0, help_text='Median Intensity - Substantia Nigra', verbose_name='Substantia Nigra - Median')),
                ('TC_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Temporal Cortex', verbose_name='Temporal Cortex - LH')),
                ('TC_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Temporal Cortex', verbose_name='Temporal Cortex - RH')),
                ('TC_Med', models.FloatField(default=0, help_text='Median Intensity - Temporal Cortex', verbose_name='Temporal Cortex - Median')),
                ('THAL_L_Med', models.FloatField(default=0, help_text='Left Hemishere Median Intensity - Thalamus', verbose_name='Thalamus - LH')),
                ('THAL_R_Med', models.FloatField(default=0, help_text='Right Hemishere Median Intensity - Thalamus', verbose_name='Thalamus - RH')),
                ('THAL_Med', models.FloatField(default=0, help_text='Median Intensity - Thalamus', verbose_name='Thalamus - Median')),
                ('geneProt', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='ibpm.geneprot', verbose_name='GeneProt')),
            ],
        ),
        migrations.CreateModel(
            name='PhosphoPeptide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peptideSequence', models.CharField(default='', help_text='Sequence of the Peptide', max_length=300, verbose_name='Peptide Sequence')),
                ('length', models.IntegerField(help_text='Length of Peptide (AA)', verbose_name='Peptide Length')),
                ('missedCleavages', models.IntegerField(help_text='Number of Missed Cleavages', verbose_name='Missed Cleavages')),
                ('phosphoAminoAcid', models.CharField(help_text='Phosphorylation Amino Acid', max_length=3, verbose_name='Phospho - Amino Acid')),
                ('phosphoPos', models.IntegerField(help_text='Phosphorylation Position', verbose_name='Phospho - Position')),
                ('AMY_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Amygdala', verbose_name='Amygdala - LH')),
                ('AMY_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Amygdala', verbose_name='Amygdala - RH')),
                ('BS_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Brain Stem', verbose_name='Brain Stem - LH')),
                ('BS_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Brain Stem', verbose_name='Brain Stem - RH')),
                ('CING_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Cingulum', verbose_name='Cingulum - LH')),
                ('CING_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Cingulum', verbose_name='Cingulum - RH')),
                ('CN_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Caudate Nucelus', verbose_name='Caudate Nucelus - LH')),
                ('CN_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Caudate Nucelus', verbose_name='Caudate Nucelus - RH')),
                ('CV_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Cerbellar Vermis', verbose_name='Cerbellar Vermis - LH')),
                ('CV_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Cerbellar Vermis', verbose_name='Cerbellar Vermis - RH')),
                ('DG_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Dentate Gyrus', verbose_name='Dentate Gyrus - LH')),
                ('DG_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Dentate Gyrus', verbose_name='Dentate Gyrus - RH')),
                ('FC_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Frontal Cortex', verbose_name='Frontal Cortex Media - LH')),
                ('FC_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Frontal Cortex', verbose_name='Frontal Cortex Media - RH')),
                ('HIP_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Hippocampus', verbose_name='Hippocampus - LH')),
                ('HIP_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Hippocampus', verbose_name='Hippocampus - RH')),
                ('MC_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Motor Cortex', verbose_name='Motor Cortex - LH')),
                ('MC_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Motor Cortex', verbose_name='Motor Cortex - RH')),
                ('SN_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Substantia Nigra', verbose_name='Substantia Nigra - LH')),
                ('SN_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Substantia Nigra', verbose_name='Substantia Nigra - RH')),
                ('SC_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Spinal Cord', verbose_name='Spinal Cord - LH')),
                ('SC_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Spinal Cord', verbose_name='Spinal Cord - RH')),
                ('THAL_L_Phos', models.FloatField(help_text='Left Hemishere Phospho Intensity - Thalamus', verbose_name='Thalamus - LH')),
                ('THAL_R_Phos', models.FloatField(help_text='Right Hemishere Phospho Intensity - Thalamus', verbose_name='Thalamus - RH')),
                ('Phospho_LH_Average', models.FloatField(help_text='Left Hemishere Phospho Intensity - Average', verbose_name='Phospho Average - LH')),
                ('Phospho_RH_Average', models.FloatField(help_text='Right Hemishere Phospho Intensity - Average', verbose_name='Phospho Average - RH')),
                ('geneProt', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='ibpm.geneprot', verbose_name='GeneProt')),
            ],
        ),
        migrations.CreateModel(
            name='Peptide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peptideSequence', models.CharField(default='', help_text='Sequence of the Peptide', max_length=300, verbose_name='Peptide Sequence')),
                ('length', models.IntegerField(help_text='Length of Peptide (AA)', verbose_name='Peptide Length')),
                ('missedCleavages', models.IntegerField(help_text='Number of Missed Cleavages', verbose_name='Missed Cleavages')),
                ('geneProt', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='ibpm.geneprot', verbose_name='GeneProt')),
            ],
        ),
    ]
