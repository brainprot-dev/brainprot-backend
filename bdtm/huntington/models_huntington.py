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

HUNTINGTON_GRADES = (
        (0, 'Control'),
        (1, 'Grade 1'),
        (2, 'Grade 2'),
        (3, 'Grade 3'),
        # TODO : Added Grade 4 corresponding to entries with 4
        (4, 'Grade 4'),
    )

# # # # # # # # # # # # # # # # # # # 
# MODELS
# # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # 
# Huntington 1
# # # # # # # # # # # # # # # # # # # 

class Huntington_1_GSE3790_U133A(models.Model):
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
    S57 = models.FloatField()
    S58 = models.FloatField()
    S59 = models.FloatField()
    S60 = models.FloatField()
    S61 = models.FloatField()
    S62 = models.FloatField()
    S63 = models.FloatField()
    S64 = models.FloatField()
    S65 = models.FloatField()
    S66 = models.FloatField()
    S67 = models.FloatField()
    S68 = models.FloatField()
    S69 = models.FloatField()
    S70 = models.FloatField()
    S71 = models.FloatField()
    S72 = models.FloatField()
    S73 = models.FloatField()
    S74 = models.FloatField()
    S75 = models.FloatField()
    S76 = models.FloatField()
    S77 = models.FloatField()
    S78 = models.FloatField()
    S79 = models.FloatField()
    S80 = models.FloatField()
    S81 = models.FloatField()
    S82 = models.FloatField()
    S83 = models.FloatField()
    S84 = models.FloatField()
    S85 = models.FloatField()
    S86 = models.FloatField()
    S87 = models.FloatField()
    S88 = models.FloatField()
    S89 = models.FloatField()
    S90 = models.FloatField()
    S91 = models.FloatField()
    S92 = models.FloatField()
    S93 = models.FloatField()
    S94 = models.FloatField()
    S95 = models.FloatField()
    S96 = models.FloatField()
    S97 = models.FloatField()
    S98 = models.FloatField()
    S99 = models.FloatField()
    S100 = models.FloatField()
    S101 = models.FloatField()
    S102 = models.FloatField()
    S103 = models.FloatField()
    S104 = models.FloatField()
    S105 = models.FloatField()
    S106 = models.FloatField()
    S107 = models.FloatField()
    S108 = models.FloatField()
    S109 = models.FloatField()
    S110 = models.FloatField()
    S111 = models.FloatField()
    S112 = models.FloatField()
    S113 = models.FloatField()
    S114 = models.FloatField()
    S115 = models.FloatField()
    S116 = models.FloatField()
    S117 = models.FloatField()
    S118 = models.FloatField()
    S119 = models.FloatField()
    S120 = models.FloatField()
    S121 = models.FloatField()
    S122 = models.FloatField()
    S123 = models.FloatField()
    S124 = models.FloatField()
    S125 = models.FloatField()
    S126 = models.FloatField()
    S127 = models.FloatField()
    S128 = models.FloatField()
    S129 = models.FloatField()
    S130 = models.FloatField()
    S131 = models.FloatField()
    S132 = models.FloatField()
    S133 = models.FloatField()
    S134 = models.FloatField()
    S135 = models.FloatField()
    S136 = models.FloatField()
    S137 = models.FloatField()
    S138 = models.FloatField()
    S139 = models.FloatField()
    S140 = models.FloatField()
    S141 = models.FloatField()
    S142 = models.FloatField()
    S143 = models.FloatField()
    S144 = models.FloatField()
    S145 = models.FloatField()
    S146 = models.FloatField()
    S147 = models.FloatField()
    S148 = models.FloatField()
    S149 = models.FloatField()
    S150 = models.FloatField()
    S151 = models.FloatField()
    S152 = models.FloatField()
    S153 = models.FloatField()
    S154 = models.FloatField()
    S155 = models.FloatField()
    S156 = models.FloatField()
    S157 = models.FloatField()
    S158 = models.FloatField()
    S159 = models.FloatField()
    S160 = models.FloatField()
    S161 = models.FloatField()
    S162 = models.FloatField()
    S163 = models.FloatField()
    S164 = models.FloatField()
    S165 = models.FloatField()
    S166 = models.FloatField()
    S167 = models.FloatField()
    S168 = models.FloatField()
    S169 = models.FloatField()
    S170 = models.FloatField()
    S171 = models.FloatField()
    S172 = models.FloatField()
    S173 = models.FloatField()
    S174 = models.FloatField()
    S175 = models.FloatField()
    S176 = models.FloatField()
    S177 = models.FloatField()
    S178 = models.FloatField()
    S179 = models.FloatField()
    S180 = models.FloatField()
    S181 = models.FloatField()
    S182 = models.FloatField()
    S183 = models.FloatField()
    S184 = models.FloatField()
    S185 = models.FloatField()
    S186 = models.FloatField()
    S187 = models.FloatField()
    S188 = models.FloatField()
    S189 = models.FloatField()
    S190 = models.FloatField()
    S191 = models.FloatField()
    S192 = models.FloatField()
    S193 = models.FloatField()
    S194 = models.FloatField()
    S195 = models.FloatField()
    S196 = models.FloatField()
    S197 = models.FloatField()
    S198 = models.FloatField()
    S199 = models.FloatField()
    S200 = models.FloatField()
    S201 = models.FloatField()

class Huntington_1_GSE3790_U133A_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)
    groupII = models.IntegerField(choices=HUNTINGTON_GRADES)

# # # # # # # # # # # # # # # # # # # 
# Huntington 2
# # # # # # # # # # # # # # # # # # #

class Huntington_2_GSE3790_U133B(models.Model):
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
    S57 = models.FloatField()
    S58 = models.FloatField()
    S59 = models.FloatField()
    S60 = models.FloatField()
    S61 = models.FloatField()
    S62 = models.FloatField()
    S63 = models.FloatField()
    S64 = models.FloatField()
    S65 = models.FloatField()
    S66 = models.FloatField()
    S67 = models.FloatField()
    S68 = models.FloatField()
    S69 = models.FloatField()
    S70 = models.FloatField()
    S71 = models.FloatField()
    S72 = models.FloatField()
    S73 = models.FloatField()
    S74 = models.FloatField()
    S75 = models.FloatField()
    S76 = models.FloatField()
    S77 = models.FloatField()
    S78 = models.FloatField()
    S79 = models.FloatField()
    S80 = models.FloatField()
    S81 = models.FloatField()
    S82 = models.FloatField()
    S83 = models.FloatField()
    S84 = models.FloatField()
    S85 = models.FloatField()
    S86 = models.FloatField()
    S87 = models.FloatField()
    S88 = models.FloatField()
    S89 = models.FloatField()
    S90 = models.FloatField()
    S91 = models.FloatField()
    S92 = models.FloatField()
    S93 = models.FloatField()
    S94 = models.FloatField()
    S95 = models.FloatField()
    S96 = models.FloatField()
    S97 = models.FloatField()
    S98 = models.FloatField()
    S99 = models.FloatField()
    S100 = models.FloatField()
    S101 = models.FloatField()
    S102 = models.FloatField()
    S103 = models.FloatField()
    S104 = models.FloatField()
    S105 = models.FloatField()
    S106 = models.FloatField()
    S107 = models.FloatField()
    S108 = models.FloatField()
    S109 = models.FloatField()
    S110 = models.FloatField()
    S111 = models.FloatField()
    S112 = models.FloatField()
    S113 = models.FloatField()
    S114 = models.FloatField()
    S115 = models.FloatField()
    S116 = models.FloatField()
    S117 = models.FloatField()
    S118 = models.FloatField()
    S119 = models.FloatField()
    S120 = models.FloatField()
    S121 = models.FloatField()
    S122 = models.FloatField()
    S123 = models.FloatField()
    S124 = models.FloatField()
    S125 = models.FloatField()
    S126 = models.FloatField()
    S127 = models.FloatField()
    S128 = models.FloatField()
    S129 = models.FloatField()
    S130 = models.FloatField()
    S131 = models.FloatField()
    S132 = models.FloatField()
    S133 = models.FloatField()
    S134 = models.FloatField()
    S135 = models.FloatField()
    S136 = models.FloatField()
    S137 = models.FloatField()
    S138 = models.FloatField()
    S139 = models.FloatField()
    S140 = models.FloatField()
    S141 = models.FloatField()
    S142 = models.FloatField()
    S143 = models.FloatField()
    S144 = models.FloatField()
    S145 = models.FloatField()
    S146 = models.FloatField()
    S147 = models.FloatField()
    S148 = models.FloatField()
    S149 = models.FloatField()
    S150 = models.FloatField()
    S151 = models.FloatField()
    S152 = models.FloatField()
    S153 = models.FloatField()
    S154 = models.FloatField()
    S155 = models.FloatField()
    S156 = models.FloatField()
    S157 = models.FloatField()
    S158 = models.FloatField()
    S159 = models.FloatField()
    S160 = models.FloatField()
    S161 = models.FloatField()
    S162 = models.FloatField()
    S163 = models.FloatField()
    S164 = models.FloatField()
    S165 = models.FloatField()
    S166 = models.FloatField()
    S167 = models.FloatField()
    S168 = models.FloatField()
    S169 = models.FloatField()
    S170 = models.FloatField()
    S171 = models.FloatField()
    S172 = models.FloatField()
    S173 = models.FloatField()
    S174 = models.FloatField()
    S175 = models.FloatField()
    S176 = models.FloatField()
    S177 = models.FloatField()
    S178 = models.FloatField()
    S179 = models.FloatField()
    S180 = models.FloatField()
    S181 = models.FloatField()
    S182 = models.FloatField()
    S183 = models.FloatField()
    S184 = models.FloatField()
    S185 = models.FloatField()
    S186 = models.FloatField()
    S187 = models.FloatField()
    S188 = models.FloatField()
    S189 = models.FloatField()
    S190 = models.FloatField()
    S191 = models.FloatField()
    S192 = models.FloatField()
    S193 = models.FloatField()
    S194 = models.FloatField()
    S195 = models.FloatField()
    S196 = models.FloatField()
    S197 = models.FloatField()
    S198 = models.FloatField()
    S199 = models.FloatField()
    S200 = models.FloatField()
    S201 = models.FloatField()
    S202 = models.FloatField()
    S203 = models.FloatField()

class Huntington_2_GSE3790_U133B_Metadata(models.Model):
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
    gender = models.IntegerField(choices=GENDERS)
    age = models.IntegerField(
        help_text="Age of Patient",
        verbose_name="Age",
        null=True,
    )
    groupI = models.IntegerField(choices=GROUP_I_CHOICES)
    groupII = models.IntegerField(choices=HUNTINGTON_GRADES)