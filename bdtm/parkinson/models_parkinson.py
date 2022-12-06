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
# Parkinson 1
# # # # # # # # # # # # # # # # # # # 

class Parkinson_1_GSE7621(models.Model):
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

class Parkinson_1_GSE7621_Metadata(models.Model):
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
# Parkinson 2
# # # # # # # # # # # # # # # # # # # 

class Parkinson_2_GSE8397_U133A(models.Model):
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

class Parkinson_2_GSE8397_U133A_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 3
# # # # # # # # # # # # # # # # # # # 

class Parkinson_3_GSE8397_U133B(models.Model):
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

class Parkinson_3_GSE8397_U133B_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 4
# # # # # # # # # # # # # # # # # # # 

class Parkinson_4_GSE19587(models.Model):
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

class Parkinson_4_GSE19587_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 5
# # # # # # # # # # # # # # # # # # # 

class Parkinson_5_GSE20141(models.Model):
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

class Parkinson_5_GSE20141_Metadata(models.Model):
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
# Parkinson 6
# # # # # # # # # # # # # # # # # # # 

class Parkinson_6_GSE20146(models.Model):
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

class Parkinson_6_GSE20146_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS, null=True)
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 7
# # # # # # # # # # # # # # # # # # # 

class Parkinson_7_GSE20163(models.Model):
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

class Parkinson_7_GSE20163_Metadata(models.Model):
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
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 8
# # # # # # # # # # # # # # # # # # # 

class Parkinson_8_GSE20164(models.Model):
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

class Parkinson_8_GSE20164_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 9
# # # # # # # # # # # # # # # # # # # 

class Parkinson_9_GSE20168(models.Model):
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

class Parkinson_9_GSE20168_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 10
# # # # # # # # # # # # # # # # # # # 

class Parkinson_10_GSE20291(models.Model):
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

class Parkinson_10_GSE20291_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 11
# # # # # # # # # # # # # # # # # # # 

class Parkinson_11_GSE20292(models.Model):
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

class Parkinson_11_GSE20292_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 12
# # # # # # # # # # # # # # # # # # # 

class Parkinson_12_GSE20314(models.Model):
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
    
class Parkinson_12_GSE20314_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 13
# # # # # # # # # # # # # # # # # # # 

class Parkinson_13_GSE20333(models.Model):
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

class Parkinson_13_GSE20333_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS, null=True)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)

# # # # # # # # # # # # # # # # # # # 
# Parkinson 14
# # # # # # # # # # # # # # # # # # # 

class Parkinson_14_GSE24378(models.Model):
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

class Parkinson_14_GSE24378_Metadata(models.Model):
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
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)
