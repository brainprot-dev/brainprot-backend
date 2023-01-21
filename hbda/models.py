from django.db import models

# Create your models here.
# Disease Model      
class Disease(models.Model):
    diseaseName = models.CharField(
        max_length=500,
        default='',
        help_text="Name of the Disease",
        verbose_name="Disease Name"
    )
    HarmonizomeQueryTerm = models.CharField(
        max_length=500,
        default='',
        help_text="Name of Disease for Harmonizome",
        verbose_name="Disease Name for Harmonizome",
        null=True
    )
    DisGeNETDiseaseId = models.CharField(
        max_length=100,
        default='',
        help_text="DisGeNet Disease ID",
        verbose_name="DisGeNet Disease ID"
    )
    numGeneDisGeNET = models.PositiveIntegerField(
        help_text="Number of Genes (DisGeNet)",
        verbose_name="No. of Genes (DisGeNet)",
    )
    numGeneHarmonizome = models.PositiveIntegerField(
        help_text="Number of Genes (Harmonizome)",
        verbose_name="No. of Genes (Harmonizome)",
        null=True
    )
    includeInBDDF = models.BooleanField(default=True)
    
    def __str__(self):
        return self.diseaseName
