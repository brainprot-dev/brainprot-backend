from django.db import models

# # # # # # # # # # # # # # # # # # # 
# Create your models here.
# For a particular disease's data set,
# Create a new class, with a new number as the suffix, followed by identifiers
# For example, if Meningioma has two datasets (GEO Accession IDs)
# There should be two classes:
# Meningioma_1_GSEXXXXXX, Meningioma_2_GSEXXXXXX
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

# # # # # # # # # # # # # # # # # # # 
# MODELS
# # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # 
# FTLD
# # # # # # # # # # # # # # # # # # # 

class FTLD_1_GSE13162(models.Model):
    probeId = models.CharField(
        max_length=200,
        help_text="The Probe ID",
        verbose_name="Probe ID",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
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

class FTLD_1_GSE13162_Metadata(models.Model):
    accession = models.CharField(
        max_length=200,
        help_text="The Probe ID",
        verbose_name="Probe ID",
    )
    sampleId = models.CharField(
        max_length=50,
        help_text="The Sample ID",
        verbose_name="Sample ID",
    )
    title = models.TextField(
        help_text="Title",
        verbose_name="Title"
    )
    sourceName = models.TextField(
        help_text="Title",
        verbose_name="Title"
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)