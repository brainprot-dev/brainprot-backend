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
    MESHID = models.CharField(
        max_length=100,
        default='',
        help_text="MESH ID",
        verbose_name="MESH ID"
    )
    umlsId = models.CharField(
        max_length=100,
        default='',
        help_text="UMLS",
        verbose_name="UMLS",
        null=True
    )
    diseaseOntology = models.CharField(
        max_length=100,
        default='',
        help_text="Disease Ontology",
        verbose_name="Disease Ontology",
        null=True
    )
    NCI = models.CharField(
        max_length=100,
        default='',
        help_text="NCI",
        verbose_name="NCI",
        null=True
    )
    GARD = models.CharField(
        max_length=100,
        default='',
        help_text="GARD",
        verbose_name="GARD",
        null=True
    )
    KEGG = models.CharField(
        max_length=100,
        default='',
        help_text="KEGG",
        verbose_name="KEGG",
        null=True
    )
    HPO = models.CharField(
        max_length=100,
        default='',
        help_text="HPO",
        verbose_name="HPO",
        null=True
    )
    monarchInitiative = models.CharField(
        max_length=100,
        default='',
        help_text="Monarch Initiative",
        verbose_name="Monarch Initiative",
        null=True
    )
    MedGenUID = models.CharField(
        max_length=100,
        default='',
        help_text="MedGen UID",
        verbose_name="MedGen UID",
        null=True
    )
    orphanet = models.CharField(
        max_length=100,
        default='',
        help_text = "Orphanet",
        verbose_name = "Orphanet",
        null=True
    )
    OMIM = models.CharField(
        max_length=100,
        default='',
        help_text = "OMIM",
        verbose_name = "OMIM",
        null=True
    )
    description = models.CharField(
        max_length=5000,
        default='',
        help_text = "Disease Description",
        verbose_name = "Description",
        null=True
    )

    def __str__(self):
        return self.diseaseName
