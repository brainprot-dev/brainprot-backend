from django.db import models

# Create your models here.

class Alzheimer(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Bionda_Score = models.FloatField(null=True)
    Unscaled_DISGENET_Score = models.FloatField(null=True)
    Unscaled_Pubpular_Score = models.FloatField(null=True)
    Unscaled_Harmonizome_Score = models.FloatField(null=True)
    Unscaled_Bionda_Score = models.FloatField(null=True)

class Amyotrophic_Lateral_Sclerosis(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Bionda_Score = models.FloatField(null=True)
    Unscaled_DISGENET_Score = models.FloatField(null=True)
    Unscaled_Pubpular_Score = models.FloatField(null=True)
    Unscaled_Harmonizome_Score = models.FloatField(null=True)
    Unscaled_Bionda_Score = models.FloatField(null=True)

class Meningioma(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Bionda_Score = models.FloatField(null=True)
    Unscaled_DISGENET_Score = models.FloatField(null=True)
    Unscaled_Pubpular_Score = models.FloatField(null=True)
    Unscaled_Harmonizome_Score = models.FloatField(null=True)
    Unscaled_Bionda_Score = models.FloatField(null=True)

class Glioma(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Bionda_Score = models.FloatField(null=True)
    Unscaled_DISGENET_Score = models.FloatField(null=True)
    Unscaled_Pubpular_Score = models.FloatField(null=True)
    Unscaled_Harmonizome_Score = models.FloatField(null=True)
    Unscaled_Bionda_Score = models.FloatField(null=True)

class Glioblastoma(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Bionda_Score = models.FloatField(null=True)
    Unscaled_DISGENET_Score = models.FloatField(null=True)
    Unscaled_Pubpular_Score = models.FloatField(null=True)
    Unscaled_Harmonizome_Score = models.FloatField(null=True)
    Unscaled_Bionda_Score = models.FloatField(null=True)

class Medulloblastoma(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Bionda_Score = models.FloatField(null=True)
    Unscaled_DISGENET_Score = models.FloatField(null=True)
    Unscaled_Pubpular_Score = models.FloatField(null=True)
    Unscaled_Harmonizome_Score = models.FloatField(null=True)
    Unscaled_Bionda_Score = models.FloatField(null=True)

class Pituitary_Adenoma(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Bionda_Score = models.FloatField(null=True)
    Unscaled_DISGENET_Score = models.FloatField(null=True)
    Unscaled_Pubpular_Score = models.FloatField(null=True)
    Unscaled_Harmonizome_Score = models.FloatField(null=True)
    Unscaled_Bionda_Score = models.FloatField(null=True)

class Parkinson(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Bionda_Score = models.FloatField(null=True)
    Unscaled_DISGENET_Score = models.FloatField(null=True)
    Unscaled_Pubpular_Score = models.FloatField(null=True)
    Unscaled_Harmonizome_Score = models.FloatField(null=True)
    Unscaled_Bionda_Score = models.FloatField(null=True)

class Huntington(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Bionda_Score = models.FloatField(null=True)
    Unscaled_DISGENET_Score = models.FloatField(null=True)
    Unscaled_Pubpular_Score = models.FloatField(null=True)
    Unscaled_Harmonizome_Score = models.FloatField(null=True)
    Unscaled_Bionda_Score = models.FloatField(null=True)

class Multiple_Sclerosis(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Bionda_Score = models.FloatField(null=True)
    Unscaled_DISGENET_Score = models.FloatField(null=True)
    Unscaled_Pubpular_Score = models.FloatField(null=True)
    Unscaled_Harmonizome_Score = models.FloatField(null=True)
    Unscaled_Bionda_Score = models.FloatField(null=True)

class Frontotemporal(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Bionda_Score = models.FloatField(null=True)
    Unscaled_DISGENET_Score = models.FloatField(null=True)
    Unscaled_Pubpular_Score = models.FloatField(null=True)
    Unscaled_Harmonizome_Score = models.FloatField(null=True)
    Unscaled_Bionda_Score = models.FloatField(null=True)