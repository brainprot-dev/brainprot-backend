from django.db import models

# # # # # # # # # # # # # # # # # # # 
# Create your models here.
# For a particular disease's data set,
# Create a new class, with a new number as the suffix, followed by identifiers
# For example, if Meningioma has two datasets (PXD Accession IDs)
# There should be two classes:
# Mengioma_1_PXDXXXXXX, Meningioma_2_PXDXXXXXX
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
        ("0", 'Male'),
        ("1", 'Female'),
    )

GROUP_I_CHOICES = (
        ("0", 'Control'),
        ("1", 'Disease'),
    )

MENINGIOMA_GRADES = (
        ("0", 'Control'),
        ("1", 'Grade 1'),
        ("2", 'Grade 2'),
        ("3", 'Grade 3'),
    )

# # # # # # # # # # # # # # # # # # # 
# MODELS
# # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # 
# Meningioma 1
# # # # # # # # # # # # # # # # # # # 

class Meningioma_1_PXD007073(models.Model):
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

class Meningioma_1_PXD007073_Metadata(models.Model):
    GROUP_III_CHOICES = (
        (0, 'Anaplastic'),
        (1, 'Atypical'),
        (2, 'Fibroplastic'),
        (3, 'Meningothelial'),
        (4, 'Transitional'),
    )
    GROUP_IV_CHOICES = (
        (0, 'Brain Stem'),
        (1, 'Frontal'),
        (2, 'Lateral posterior fossa'),
        (3, 'Occipital'),
        (4, 'Olfactory groove'),
        (5, 'Parafalcine'),
        (6, 'Parasagittal'),
        (7, 'Parietal'),
        (8, 'Sphenoid wing'),
    )
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
    groupII = models.IntegerField(choices=MENINGIOMA_GRADES)
    groupIII = models.IntegerField(choices=GROUP_III_CHOICES, null=True)
    groupIV = models.IntegerField(choices=GROUP_IV_CHOICES, null=True)

# # # # # # # # # # # # # # # # # # # 
# Meningioma 2
# # # # # # # # # # # # # # # # # # # 

class Meningioma_2_PXD014852(models.Model):
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

class Meningioma_2_PXD014852_Metadata(models.Model):
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
    groupII = models.IntegerField(choices=MENINGIOMA_GRADES)