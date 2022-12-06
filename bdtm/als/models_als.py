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
# ALS 1
# # # # # # # # # # # # # # # # # # # 

class ALS_1_GSE19332(models.Model):
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

class ALS_1_GSE19332_Metadata(models.Model):
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

# # # # # # # # # # # # # # # # # # # 
# ALS 2
# # # # # # # # # # # # # # # # # # # 

class ALS_2_GSE20589(models.Model):
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

class ALS_2_GSE20589_Metadata(models.Model):
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
    
# # # # # # # # # # # # # # # # # # # 
# ALS 3
# # # # # # # # # # # # # # # # # # # 

class ALS_3_GSE68605(models.Model):
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
    
class ALS_3_GSE68605_Metadata(models.Model):
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