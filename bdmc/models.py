from django.db import models

# Create your models here.


# Alzheimer's Disease
class D000544(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Amyotrophic Lateral Sclerosis
class D000690(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
        
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Angelman Syndrome
class D017204(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
        
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Anxiety Disorder
class D001008(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
        
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Aphasia
class D001037(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
        
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Ataxia Telangiectasia
class D001260(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Attention deficit hyperactivity disorder
class D001289(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Autism Spectrum Disorder
class D000067877(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Bipolar Disorder
class D001714(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Cerebral Infarction
class D002544(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Cerebral Ischemia/Transient Cerebral Ischemia
class D002545(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Cerebral Palsy
class D002547(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Creutzfeldt Jakob Disease
class D007562(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Dementia (Non-Alzheimer)
class D003704(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Down Syndrome
class D004314(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Dyslexia
class D004410(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Dystonia
class D004421(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Encephalitis
class D004660(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Encephalomyelitis
class D004679(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Epilepsy
class D004827(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Essential Tremor
class D020329(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Fragile X Syndrome
class D005600(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Friedreich Ataxia
class D005621(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Frontotemporal Dementia
class D057180(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Frontotemporal Lobar Degeneration
class D057174(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Gaucher Disease
class D005776(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Gilles De La Tourette Syndrome
class D005879(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Glioblastoma
class D005909(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Glioma
class D005910(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Huntington's Disease
class D006816(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Hydrocephalus
class D006849(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Intellectual Disability
class D008607(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Intracranial Aneurysm
class D002532(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Medulloblastoma
class D008527(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Meningitis
class D008581(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Meningioma
class D008579(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Motor Neurone Disease
class D016472(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Multiple Sclerosis
class D009103(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Muscular Dystrophy
class D009136(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# narcolepsy
class D009290(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Neurilemmoma
class D009442(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Neuroblastoma
class D009447(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Neuroendocrine Tumor
class D018358(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Neurofibromatosis
class D017253(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Panic Disorder
class D016584(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Paraganglioma
class D010235(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Parkinson's Disease
class D010300(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Pituitary Adenoma
class D049912(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Plexiform Neurofibroma
class D018318(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Post-traumatic Stress Disorder
class D013313(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Prader-Willi Syndrome
class D011218(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Prion Disease
class D017096(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Rett Syndrome
class D015518(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Schizophrenia
class D012559(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Tay-Sachs Disease
class D013661(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)


# Tuberous Sclerosis
class D014402(models.Model):
    SwissProt_Accessions = models.CharField(
        max_length=200,
        help_text="SwissProt Accession",
        verbose_name="SwissProt Accession",
        default="",
    )
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    DISGENET_Score = models.FloatField(null=True)
    Harmonizome_Score = models.FloatField(null=True)
    Pubpular_Score = models.FloatField(null=True)
    CTD_Score = models.FloatField(null=True)
    D2_Score = models.FloatField(null=True)
    DH_Score = models.FloatField(null=True)
    DP_Score = models.FloatField(null=True)
    DC_Score = models.FloatField(null=True)
    HP_Score = models.FloatField(null=True)
    HC_Score = models.FloatField(null=True)
    PC_Score = models.FloatField(null=True)
    D2D_Score = models.FloatField(null=True)
    D2H_Score = models.FloatField(null=True)
    D2P_Score = models.FloatField(null=True)
    D2C_Score = models.FloatField(null=True)
    BDMC_Score = models.FloatField(null=True)
    Frequency = models.IntegerField(null=True)
    CTD_Marker = models.IntegerField(null=True)
    eDGAR_Marker = models.IntegerField(null=True)
    BIONDA_Marker = models.IntegerField(null=True)
    Dis_2_Marker = models.IntegerField(null=True)
