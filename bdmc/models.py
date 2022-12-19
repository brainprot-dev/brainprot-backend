from django.db import models

# Create your models here.

class Alzheimer(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField()
    Pubpular_Score = models.FloatField()
    Harmonizome_Score = models.FloatField()
    Bionda_Score = models.FloatField()

class Amyotrophic_Lateral_Sclerosis(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField()
    Pubpular_Score = models.FloatField()
    Harmonizome_Score = models.FloatField()
    Bionda_Score = models.FloatField()

class Meningioma(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField()
    Pubpular_Score = models.FloatField()
    Harmonizome_Score = models.FloatField()
    Bionda_Score = models.FloatField()

class Glioma(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField()
    Pubpular_Score = models.FloatField()
    Harmonizome_Score = models.FloatField()
    Bionda_Score = models.FloatField()

class Glioblastoma(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField()
    Pubpular_Score = models.FloatField()
    Harmonizome_Score = models.FloatField()
    Bionda_Score = models.FloatField()

class Medulloblastoma(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField()
    Pubpular_Score = models.FloatField()
    Harmonizome_Score = models.FloatField()
    Bionda_Score = models.FloatField()

class Pituitary_Adenoma(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField()
    Pubpular_Score = models.FloatField()
    Harmonizome_Score = models.FloatField()
    Bionda_Score = models.FloatField()

class Parkinson(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField()
    Pubpular_Score = models.FloatField()
    Harmonizome_Score = models.FloatField()
    Bionda_Score = models.FloatField()

class Huntington(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField()
    Pubpular_Score = models.FloatField()
    Harmonizome_Score = models.FloatField()
    Bionda_Score = models.FloatField()

class Multiple_Sclerosis(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField()
    Pubpular_Score = models.FloatField()
    Harmonizome_Score = models.FloatField()
    Bionda_Score = models.FloatField()

class Frontotemporal(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default='',
    )
    DISGENET_Score = models.FloatField()
    Pubpular_Score = models.FloatField()
    Harmonizome_Score = models.FloatField()
    Bionda_Score = models.FloatField()