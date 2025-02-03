from django.db import models

# # # # # # # # # # # # # # # # # # # 
# Create your models here.
# For a particular disease's data set,
# Create a new class, with a new number as the suffix, followed by identifiers
# For example, if Parkinson has two datasets (PXD Accession IDs)
# There should be two classes:
# Mengioma_1_PXDXXXXXX, Parkinson_2_PXDXXXXXX
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

Parkinson_GRADES = (
        (0, 'Control'),
        (1, 'Grade 1'),
        (2, 'Grade 2'),
        (3, 'Grade 3'),
    )

# # # # # # # # # # # # # # # # # # # 
# MODELS
# # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # 
# Parkinson 1
# # # # # # # # # # # # # # # # # # # 

class Parkinson_1_PXD008036(models.Model):
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
#    S25 = models.FloatField()

# class Parkinson_1_PXD008036_Unprocessed(models.Model):
#     proteinId = models.CharField(
#         max_length=200,
#         help_text="UniProt Protein ID",
#         verbose_name="Protein ID",
#         default='',
#     )
#     S1 = models.FloatField()
#     S2 = models.FloatField()
#     S3 = models.FloatField()
#     S4 = models.FloatField()
#     S5 = models.FloatField()
#     S6 = models.FloatField()
#     S7 = models.FloatField()
#     S8 = models.FloatField()
#     S9 = models.FloatField()
#     S10 = models.FloatField()
#     S11 = models.FloatField()
#     S12 = models.FloatField()
#     S13 = models.FloatField()
#     S14 = models.FloatField()
#     S15 = models.FloatField()
#     S16 = models.FloatField()
#     S17 = models.FloatField()
#     S18 = models.FloatField()
#     S19 = models.FloatField()
#     S20 = models.FloatField()
#     S21 = models.FloatField()
#     S22 = models.FloatField()
#     S23 = models.FloatField()
#     S24 = models.FloatField()
#     S25 = models.FloatField()


class Parkinson_1_PXD008036_Metadata(models.Model):
    # GROUP_III_CHOICES = (
    #     (0, 'Anaplastic'),
    #     (1, 'Atypical'),
    #     (2, 'Fibroplastic'),
    #     (3, 'Meningothelial'),
    #     (4, 'Transitional'),
    # )
    # GROUP_IV_CHOICES = (
    #     (0, 'Brain Stem'),
    #     (1, 'Frontal'),
    #     (2, 'Lateral posterior fossa'),
    #     (3, 'Occipital'),
    #     (4, 'Olfactory groove'),
    #     (5, 'Parafalcine'),
    #     (6, 'Parasagittal'),
    #     (7, 'Parietal'),
    #     (8, 'Sphenoid wing'),
    # )
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
    # groupII = models.IntegerField(choices=Parkinson_GRADES)
    # groupIII = models.IntegerField(choices=GROUP_III_CHOICES, null=True)
    # groupIV = models.IntegerField(choices=GROUP_IV_CHOICES, null=True)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 2
# # # # # # # # # # # # # # # # # # # 

class Parkinson_2_PXD022092(models.Model):
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

    # S1_Raw = models.FloatField()
    # S2_Raw = models.FloatField()
    # S3_Raw = models.FloatField()
    # S4_Raw = models.FloatField()
    # S5_Raw = models.FloatField()
    # S6_Raw = models.FloatField()
    # S7_Raw = models.FloatField()
    # S8_Raw = models.FloatField()
    # S9_Raw = models.FloatField()
    # S10_Raw = models.FloatField()
    # S11_Raw = models.FloatField()
    # S12_Raw = models.FloatField()
    # S13_Raw = models.FloatField()
    # S14_Raw = models.FloatField()
    # S15_Raw = models.FloatField()
    # S16_Raw = models.FloatField()
    # S17_Raw = models.FloatField()
    # S18_Raw = models.FloatField()
    # S19_Raw = models.FloatField()
    # S20_Raw = models.FloatField()
    # S21_Raw = models.FloatField()
    # S22_Raw = models.FloatField()
    # S23_Raw = models.FloatField()
    # S24_Raw = models.FloatField()
    # S25_Raw = models.FloatField()
    # S26_Raw = models.FloatField()
    # S27_Raw = models.FloatField()
    # S28_Raw = models.FloatField()
    # S29_Raw = models.FloatField()

# class Parkinson_2_PXD022092_Unprocessed(models.Model):
#     proteinId = models.CharField(
#         max_length=200,
#         help_text="UniProt Protein ID",
#         verbose_name="Protein ID",
#         default='',
#     )
#     S1 = models.FloatField()
#     S2 = models.FloatField()
#     S3 = models.FloatField()
#     S4 = models.FloatField()
#     S5 = models.FloatField()
#     S6 = models.FloatField()
#     S7 = models.FloatField()
#     S8 = models.FloatField()
#     S9 = models.FloatField()
#     S10 = models.FloatField()
#     S11 = models.FloatField()
#     S12 = models.FloatField()
#     S13 = models.FloatField()
#     S14 = models.FloatField()
#     S15 = models.FloatField()
#     S16 = models.FloatField()
#     S17 = models.FloatField()
#     S18 = models.FloatField()
#     S19 = models.FloatField()
#     S20 = models.FloatField()
#     S21 = models.FloatField()
#     S22 = models.FloatField()
#     S23 = models.FloatField()
#     S24 = models.FloatField()
#     S25 = models.FloatField()
#     S26 = models.FloatField()
#     S27 = models.FloatField()
#     S28 = models.FloatField()
#     S29 = models.FloatField()

class Parkinson_2_PXD022092_Metadata(models.Model):
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
    # groupII = models.IntegerField(choices=Parkinson_GRADES)


# # # # # # # # # # # # # # # # # # # 
# Parkinson 3
# # # # # # # # # # # # # # # # # # # 

class Parkinson_3_PXD024998(models.Model):
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

class Parkinson_3_PXD024998_Metadata(models.Model):
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
    groupI = models.IntegerField(choices=GROUP_I_CHOICES, null=True)
