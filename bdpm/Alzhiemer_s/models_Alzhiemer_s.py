from django.db import models

# # # # # # # # # # # # # # # # # # # 
# Create your models here.
# For a particular disease's data set,
# Create a new class, with a new number as the suffix, followed by identifiers
# For example, if Alzhiemer_s has two datasets (PXD Accession IDs)
# There should be two classes:
# Mengioma_1_PXDXXXXXX, Alzhiemer_s_2_PXDXXXXXX
# # # # # # # # # # # # # # # # # # # 
# REGARDING METADATA
# # # # # # # # # # # # # # # # # # #
# The Metadata for each data-set should be separate,
# The name should follow the data model class, followed by '_Metadata' at the end
# We will be linking the two tables (Dataset and Metadata)
# Using the SAMPLE IDs
# Whose naming is S1, S2, S3, S4, ...
# # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # 
# COMMON CHOICES
# # # # # # # # # # # # # # # # # # # 

GENDERS = (
        (0, 'Male'),
        (1, 'Female'),
    )

GROUP_I_CHOICES = (
        (0, 'Control'),
        (1, 'Disease'),
    )

GROUP_II_CHOICES = (
        (0, 'CA1'),
        (1, 'Entorhinal cortex'),
        (2,'Hippocampus'),
        (3,'Perirhinal cortex')
    )


# Alzhiemer_s_GRADES = (
#         (0, 'Control'),
#         (1, 'Grade 1'),
#         (2, 'Grade 2'),
#         (3, 'Grade 3'),
#     )

# # # # # # # # # # # # # # # # # # # 
# MODELS
# # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 1
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_1_PXD009199(models.Model):
    proteinId = models.CharField(
        max_length=200,
        help_text="UniProt Protein ID",
        verbose_name="Protein ID",
        default='',
    )
    S1 = models.FloatField()
    S2 = models.FloatField()
    S3 = models.FloatField()
    S4 = models.FloatField()
    S5 = models.FloatField()
    S6 = models.FloatField()
    S7 = models.FloatField()
    S8 = models.FloatField()
    S9 = models.FloatField()
    S10 = models.FloatField()


class Alzhiemer_s_1_PXD009199_Metadata(models.Model):
    sourceName = models.TextField(
        help_text="Name of Source File",
        verbose_name="Source Name"
    )
    sampleId = models.CharField(
        max_length=50,
        help_text="The Sample ID",
        verbose_name="Sample ID",
    )
   
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 2
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_2_PXD014376(models.Model):
    proteinId = models.CharField(
        max_length=200,
        help_text="UniProt Protein ID",
        verbose_name="Protein ID",
        default='',
    )
    S1 = models.FloatField()
    S2 = models.FloatField()
    S3 = models.FloatField()
    S4 = models.FloatField()
    S5 = models.FloatField()
    S6 = models.FloatField()
    S7 = models.FloatField()
    S8 = models.FloatField()
    S9 = models.FloatField()
    S10 = models.FloatField()
    S11 = models.FloatField()
    S12 = models.FloatField()
    S13 = models.FloatField()
    S14 = models.FloatField()
    S15 = models.FloatField()
    S16 = models.FloatField()
    S17 = models.FloatField()
    S18 = models.FloatField()

class Alzhiemer_s_2_PXD014376_Metadata(models.Model):
    sourceName = models.TextField(
        help_text="Name of Source File",
        verbose_name="Source Name"
    )
    sampleId = models.CharField(
        max_length=50,
        help_text="The Sample ID",
        verbose_name="Sample ID",
    )
    sampleName = models.TextField(
        help_text="Name of Sample",
        verbose_name="Sample Name"
    )

    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )

    gender = models.IntegerField(choices=GENDERS, null=True)
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)


# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 3
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_3_PXD037133(models.Model):
    proteinId = models.CharField(
        max_length=200,
        help_text="UniProt Protein ID",
        verbose_name="Protein ID",
        default='',
    )
    S1 = models.FloatField()
    S2 = models.FloatField()
    S3 = models.FloatField()
    S4 = models.FloatField()
    S5 = models.FloatField()
    S6 = models.FloatField()
    S7 = models.FloatField()
    S8 = models.FloatField()
    S9 = models.FloatField()
    S10 = models.FloatField()
    S11 = models.FloatField()
    S12 = models.FloatField()
    S13 = models.FloatField()
    S14 = models.FloatField()
    S15 = models.FloatField()
    S16 = models.FloatField()

class Alzhiemer_s_3_PXD037133_Metadata(models.Model):
    sourceName = models.TextField(
        help_text="Name of Source File",
        verbose_name="Source Name"
    )
    sampleId = models.CharField(
        max_length=50,
        help_text="The Sample ID",
        verbose_name="Sample ID",
    )
    sampleName = models.TextField(
        help_text="Name of Sample",
        verbose_name="Sample Name"
    )
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES, null=True)
    


# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 4
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_4_PXD005319(models.Model):
    proteinId = models.CharField(
        max_length=200,
        help_text="UniProt Protein ID",
        verbose_name="Protein ID",
        default='',
    )
    S1 = models.FloatField()
    S2 = models.FloatField()
    S3 = models.FloatField()
    S4 = models.FloatField()
    S5 = models.FloatField()
    S6 = models.FloatField()
    S7 = models.FloatField()
    S8 = models.FloatField()
    S9 = models.FloatField()
    S10 = models.FloatField()
    S11 = models.FloatField()
    S12 = models.FloatField()
    S13 = models.FloatField()
    S14 = models.FloatField()
    S15 = models.FloatField()
    S16 = models.FloatField()

class Alzhiemer_s_4_PXD005319_Metadata(models.Model):
    sourceName = models.TextField(
        help_text="Name of Source File",
        verbose_name="Source Name"
    )
    sampleId = models.CharField(
        max_length=50,
        help_text="The Sample ID",
        verbose_name="Sample ID",
    )
    sampleName = models.TextField(
        help_text="Name of Sample",
        verbose_name="Sample Name"
    )
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES, null=True)




# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 5
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_5_PXD005321(models.Model):
    proteinId = models.CharField(
        max_length=200,
        help_text="UniProt Protein ID",
        verbose_name="Protein ID",
        default='',
    )
    S1 = models.FloatField()
    S2 = models.FloatField()
    S3 = models.FloatField()
    S4 = models.FloatField()
    S5 = models.FloatField()
    S6 = models.FloatField()
    S7 = models.FloatField()
    S8 = models.FloatField()
    S9 = models.FloatField()
    S10 = models.FloatField()
    S11 = models.FloatField()
    S12 = models.FloatField()
    S13 = models.FloatField()
    S14 = models.FloatField()
    S15 = models.FloatField()
    S16 = models.FloatField()
    S17 = models.FloatField()
    S18 = models.FloatField()

class Alzhiemer_s_5_PXD005321_Metadata(models.Model):
    sourceName = models.TextField(
        help_text="Name of Source File",
        verbose_name="Source Name"
    )
    sampleId = models.CharField(
        max_length=50,
        help_text="The Sample ID",
        verbose_name="Sample ID",
    )
    sampleName = models.TextField(
        help_text="Name of Sample",
        verbose_name="Sample Name"
    )
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES, null=True)


# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 6
# # # # # # # # # # # # # # # # # # # 

""" class Alzhiemer_s_6_PXD021645(models.Model):
    proteinId = models.CharField(
        max_length=200,
        help_text="UniProt Protein ID",
        verbose_name="Protein ID",
        default='',
    )
    S1 = models.FloatField()
    S2 = models.FloatField()
    S3 = models.FloatField()
    S4 = models.FloatField()
    S5 = models.FloatField()
    S6 = models.FloatField()
    S7 = models.FloatField()
    S8 = models.FloatField()
    S9 = models.FloatField()
    S10 = models.FloatField()
    S11 = models.FloatField()
    S12 = models.FloatField()
    S13 = models.FloatField()
    S14 = models.FloatField()
    S15 = models.FloatField()

class Alzhiemer_s_6_PXD021645_Metadata(models.Model):
    sourceName = models.TextField(
        help_text="Name of Source File",
        verbose_name="Source Name"
    )
    sampleId = models.CharField(
        max_length=50,
        help_text="The Sample ID",
        verbose_name="Sample ID",
    )
    sampleName = models.TextField(
        help_text="Name of Sample",
        verbose_name="Sample Name"
    )
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES, null=True)

 """

# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 7
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_7_PXD023199(models.Model):
    proteinId = models.CharField(
        max_length=200,
        help_text="UniProt Protein ID",
        verbose_name="Protein ID",
        default='',
    )
    S1 = models.FloatField()
    S2 = models.FloatField()
    S3 = models.FloatField()
    S4 = models.FloatField()
    S5 = models.FloatField()
    S6 = models.FloatField()
    S7 = models.FloatField()
    S8 = models.FloatField()
    S9 = models.FloatField()
    S10 = models.FloatField()
    S11 = models.FloatField()
    S12 = models.FloatField()
    S13 = models.FloatField()
    S14 = models.FloatField()
    S15 = models.FloatField()
    S16 = models.FloatField()
    S17 = models.FloatField()
    S18 = models.FloatField()
    S19 = models.FloatField()
    S20 = models.FloatField()
    S21 = models.FloatField()
    S22 = models.FloatField()
    S23 = models.FloatField()
    S24 = models.FloatField()
    S25 = models.FloatField()
    S26 = models.FloatField()
    S27 = models.FloatField()
    S28 = models.FloatField()
    S29 = models.FloatField()
    S30 = models.FloatField()
    S31 = models.FloatField()
    S32 = models.FloatField()
    S33 = models.FloatField()
    S34 = models.FloatField()
    S35 = models.FloatField()   

class Alzhiemer_s_7_PXD023199_Metadata(models.Model):
    sourceName = models.TextField(
        help_text="Name of Source File",
        verbose_name="Source Name"
    )
    sampleId = models.CharField(
        max_length=50,
        help_text="The Sample ID",
        verbose_name="Sample ID",
    )
    sampleName = models.TextField(
        help_text="Name of Sample",
        verbose_name="Sample Name"
    )
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES, null=True)




# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 8
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_8_PXD027173(models.Model):
    proteinId = models.CharField(
        max_length=200,
        help_text="UniProt Protein ID",
        verbose_name="Protein ID",
        default='',
    )
    S1 = models.FloatField()
    S2 = models.FloatField()
    S3 = models.FloatField()
    S4 = models.FloatField()
    S5 = models.FloatField()
    S6 = models.FloatField()
    S7 = models.FloatField()
    S8 = models.FloatField()
    S9 = models.FloatField()
    S10 = models.FloatField()
    S11 = models.FloatField()
    S12 = models.FloatField()
    S13 = models.FloatField()
    S14 = models.FloatField()
    S15 = models.FloatField()
    S16 = models.FloatField()
    S17 = models.FloatField()
    S18 = models.FloatField()
    S19 = models.FloatField()
    S20 = models.FloatField()
    S21 = models.FloatField()
    S22 = models.FloatField()
    S23 = models.FloatField()
    S24 = models.FloatField()
    S25 = models.FloatField()
    S26 = models.FloatField()
    S27 = models.FloatField()
    S28 = models.FloatField()
    S29 = models.FloatField()
    S30 = models.FloatField()
    S31 = models.FloatField()
    S32 = models.FloatField()
    S33 = models.FloatField()
    S34 = models.FloatField()
    S35 = models.FloatField()
    S36 = models.FloatField()
    S37 = models.FloatField()
    S38 = models.FloatField()
    S39 = models.FloatField()
    S40 = models.FloatField()
    S41 = models.FloatField()
    S42 = models.FloatField()
    S43 = models.FloatField()
    S44 = models.FloatField()
    S45 = models.FloatField()
    S46 = models.FloatField()
    S47 = models.FloatField()
    S48 = models.FloatField()
    S49 = models.FloatField()
    S50 = models.FloatField()
    S51 = models.FloatField()
    S52 = models.FloatField()
    S53 = models.FloatField()
    S54 = models.FloatField()
    S55 = models.FloatField()
    S56 = models.FloatField()
    S57 = models.FloatField()
    S58 = models.FloatField()

class Alzhiemer_s_8_PXD027173_Metadata(models.Model):
    sourceName = models.TextField(
        help_text="Name of Source File",
        verbose_name="Source Name"
    )
    sampleId = models.CharField(
        max_length=50,
        help_text="The Sample ID",
        verbose_name="Sample ID",
    )
    sampleName = models.TextField(
        help_text="Name of Sample",
        verbose_name="Sample Name"
    )
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)
    groupII = models.IntegerField(choices=GROUP_II_CHOICES)
