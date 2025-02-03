from django.db import models

# Alzheimer's Disease
class D000544(models.Model):
    Uniprot = models.CharField(
        max_length=300,
        help_text="Uniprot",
        verbose_name="Uniprot",
        default="",
    )
    Smiles = models.CharField(
        max_length=2000,
        help_text="Smiles",
        verbose_name="Smiles",
        default="",
    )
    Score = models.FloatField(null=True)
    MOA = models.CharField(
        max_length=300,
        help_text="MOA",
        verbose_name="MOA",
        default="",
    )
    Investigation = models.CharField(
        max_length=300,
        help_text="Investigation",
        verbose_name="Investigation",
        default="",
    )
    ChemblID = models.CharField(
        max_length=300,
        help_text="ChemblID",
        verbose_name="ChemblID",
        default="",
    )
    Toxicity = models.CharField(
        max_length=300,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default="",
    )
    Drug_Name = models.CharField(
        max_length=2000,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default="",
    )
    clue_moa = models.CharField(
        max_length=300,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default="",
    )
    clinical_phase = models.CharField(
        max_length=300,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )
    Source = models.CharField(
        max_length=300,
        help_text="Source",
        verbose_name="Source",
        default="",
    )
    pref_name = models.CharField(
        max_length=300,
        help_text="pref_name",
        verbose_name="pref_name",
        default="",
    )
    Gene_Name = models.CharField(
        max_length=300,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )

# Amyotrophic Lateral Sclerosis
class D000690(models.Model):
    Uniprot = models.CharField(
        max_length=300,
        help_text="Uniprot",
        verbose_name="Uniprot",
        default="",
    )
    Smiles = models.CharField(
        max_length=2000,
        help_text="Smiles",
        verbose_name="Smiles",
        default="",
    )
    Score = models.FloatField(null=True)
    MOA = models.CharField(
        max_length=300,
        help_text="MOA",
        verbose_name="MOA",
        default="",
    )
    Investigation = models.CharField(
        max_length=300,
        help_text="Investigation",
        verbose_name="Investigation",
        default="",
    )
    ChemblID = models.CharField(
        max_length=300,
        help_text="ChemblID",
        verbose_name="ChemblID",
        default="",
    )
    Toxicity = models.CharField(
        max_length=300,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default="",
    )
    Drug_Name = models.CharField(
        max_length=2000,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default="",
    )
    clue_moa = models.CharField(
        max_length=300,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default="",
    )
    clinical_phase = models.CharField(
        max_length=300,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )
    Source = models.CharField(
        max_length=300,
        help_text="Source",
        verbose_name="Source",
        default="",
    )
    pref_name = models.CharField(
        max_length=300,
        help_text="pref_name",
        verbose_name="pref_name",
        default="",
    )
    Gene_Name = models.CharField(
        max_length=300,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )

# Frontotemporal Lobar Degeneration
class D057174(models.Model):
    Uniprot = models.CharField(
        max_length=300,
        help_text="Uniprot",
        verbose_name="Uniprot",
        default="",
    )
    Smiles = models.CharField(
        max_length=2000,
        help_text="Smiles",
        verbose_name="Smiles",
        default="",
    )
    Score = models.FloatField(null=True)
    MOA = models.CharField(
        max_length=300,
        help_text="MOA",
        verbose_name="MOA",
        default="",
    )
    Investigation = models.CharField(
        max_length=300,
        help_text="Investigation",
        verbose_name="Investigation",
        default="",
    )
    ChemblID = models.CharField(
        max_length=300,
        help_text="ChemblID",
        verbose_name="ChemblID",
        default="",
    )
    Toxicity = models.CharField(
        max_length=300,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default="",
    )
    Drug_Name = models.CharField(
        max_length=2000,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default="",
    )
    clue_moa = models.CharField(
        max_length=300,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default="",
    )
    clinical_phase = models.CharField(
        max_length=300,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )
    Source = models.CharField(
        max_length=300,
        help_text="Source",
        verbose_name="Source",
        default="",
    )
    pref_name = models.CharField(
        max_length=300,
        help_text="pref_name",
        verbose_name="pref_name",
        default="",
    )
    Gene_Name = models.CharField(
        max_length=300,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )

# Glioblastoma
class D005909(models.Model):
    Uniprot = models.CharField(
        max_length=300,
        help_text="Uniprot",
        verbose_name="Uniprot",
        default="",
    )
    Smiles = models.CharField(
        max_length=2000,
        help_text="Smiles",
        verbose_name="Smiles",
        default="",
    )
    Score = models.FloatField(null=True)
    MOA = models.CharField(
        max_length=300,
        help_text="MOA",
        verbose_name="MOA",
        default="",
    )
    Investigation = models.CharField(
        max_length=300,
        help_text="Investigation",
        verbose_name="Investigation",
        default="",
    )
    ChemblID = models.CharField(
        max_length=300,
        help_text="ChemblID",
        verbose_name="ChemblID",
        default="",
    )
    Toxicity = models.CharField(
        max_length=300,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default="",
    )
    Drug_Name = models.CharField(
        max_length=2000,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default="",
    )
    clue_moa = models.CharField(
        max_length=300,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default="",
    )
    clinical_phase = models.CharField(
        max_length=300,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )
    Source = models.CharField(
        max_length=300,
        help_text="Source",
        verbose_name="Source",
        default="",
    )
    pref_name = models.CharField(
        max_length=300,
        help_text="pref_name",
        verbose_name="pref_name",
        default="",
    )
    Gene_Name = models.CharField(
        max_length=300,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )

# Glioma
class D005910(models.Model):
    Uniprot = models.CharField(
        max_length=300,
        help_text="Uniprot",
        verbose_name="Uniprot",
        default="",
    )
    Smiles = models.CharField(
        max_length=2000,
        help_text="Smiles",
        verbose_name="Smiles",
        default="",
    )
    Score = models.FloatField(null=True)
    MOA = models.CharField(
        max_length=300,
        help_text="MOA",
        verbose_name="MOA",
        default="",
    )
    Investigation = models.CharField(
        max_length=300,
        help_text="Investigation",
        verbose_name="Investigation",
        default="",
    )
    ChemblID = models.CharField(
        max_length=300,
        help_text="ChemblID",
        verbose_name="ChemblID",
        default="",
    )
    Toxicity = models.CharField(
        max_length=300,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default="",
    )
    Drug_Name = models.CharField(
        max_length=2000,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default="",
    )
    clue_moa = models.CharField(
        max_length=300,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default="",
    )
    clinical_phase = models.CharField(
        max_length=300,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )
    Source = models.CharField(
        max_length=300,
        help_text="Source",
        verbose_name="Source",
        default="",
    )
    pref_name = models.CharField(
        max_length=300,
        help_text="pref_name",
        verbose_name="pref_name",
        default="",
    )
    Gene_Name = models.CharField(
        max_length=300,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )

# Huntington's Disease
class D006816(models.Model):
    Uniprot = models.CharField(
        max_length=300,
        help_text="Uniprot",
        verbose_name="Uniprot",
        default="",
    )
    Smiles = models.CharField(
        max_length=2000,
        help_text="Smiles",
        verbose_name="Smiles",
        default="",
    )
    Score = models.FloatField(null=True)
    MOA = models.CharField(
        max_length=300,
        help_text="MOA",
        verbose_name="MOA",
        default="",
    )
    Investigation = models.CharField(
        max_length=300,
        help_text="Investigation",
        verbose_name="Investigation",
        default="",
    )
    ChemblID = models.CharField(
        max_length=300,
        help_text="ChemblID",
        verbose_name="ChemblID",
        default="",
    )
    Toxicity = models.CharField(
        max_length=300,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default="",
    )
    Drug_Name = models.CharField(
        max_length=2000,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default="",
    )
    clue_moa = models.CharField(
        max_length=300,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default="",
    )
    clinical_phase = models.CharField(
        max_length=300,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )
    Source = models.CharField(
        max_length=300,
        help_text="Source",
        verbose_name="Source",
        default="",
    )
    pref_name = models.CharField(
        max_length=300,
        help_text="pref_name",
        verbose_name="pref_name",
        default="",
    )
    Gene_Name = models.CharField(
        max_length=300,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )

# Medulloblastoma
class D008527(models.Model):
    Uniprot = models.CharField(
        max_length=300,
        help_text="Uniprot",
        verbose_name="Uniprot",
        default="",
    )
    Smiles = models.CharField(
        max_length=2000,
        help_text="Smiles",
        verbose_name="Smiles",
        default="",
    )
    Score = models.FloatField(null=True)
    MOA = models.CharField(
        max_length=300,
        help_text="MOA",
        verbose_name="MOA",
        default="",
    )
    Investigation = models.CharField(
        max_length=300,
        help_text="Investigation",
        verbose_name="Investigation",
        default="",
    )
    ChemblID = models.CharField(
        max_length=300,
        help_text="ChemblID",
        verbose_name="ChemblID",
        default="",
    )
    Toxicity = models.CharField(
        max_length=300,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default="",
    )
    Drug_Name = models.CharField(
        max_length=2000,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default="",
    )
    clue_moa = models.CharField(
        max_length=300,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default="",
    )
    clinical_phase = models.CharField(
        max_length=300,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )
    Source = models.CharField(
        max_length=300,
        help_text="Source",
        verbose_name="Source",
        default="",
    )
    pref_name = models.CharField(
        max_length=300,
        help_text="pref_name",
        verbose_name="pref_name",
        default="",
    )
    Gene_Name = models.CharField(
        max_length=300,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )

# Meningioma
class D008579(models.Model):
    Uniprot = models.CharField(
        max_length=300,
        help_text="Uniprot",
        verbose_name="Uniprot",
        default="",
    )
    Smiles = models.CharField(
        max_length=2000,
        help_text="Smiles",
        verbose_name="Smiles",
        default="",
    )
    Score = models.FloatField(null=True)
    MOA = models.CharField(
        max_length=300,
        help_text="MOA",
        verbose_name="MOA",
        default="",
    )
    Investigation = models.CharField(
        max_length=300,
        help_text="Investigation",
        verbose_name="Investigation",
        default="",
    )
    ChemblID = models.CharField(
        max_length=300,
        help_text="ChemblID",
        verbose_name="ChemblID",
        default="",
    )
    Toxicity = models.CharField(
        max_length=300,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default="",
    )
    Drug_Name = models.CharField(
        max_length=2000,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default="",
    )
    clue_moa = models.CharField(
        max_length=300,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default="",
    )
    clinical_phase = models.CharField(
        max_length=300,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )
    Source = models.CharField(
        max_length=300,
        help_text="Source",
        verbose_name="Source",
        default="",
    )
    pref_name = models.CharField(
        max_length=300,
        help_text="pref_name",
        verbose_name="pref_name",
        default="",
    )
    Gene_Name = models.CharField(
        max_length=300,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )

# Multiple Sclerosis
class D009103(models.Model):
    Uniprot = models.CharField(
        max_length=300,
        help_text="Uniprot",
        verbose_name="Uniprot",
        default="",
    )
    Smiles = models.CharField(
        max_length=2000,
        help_text="Smiles",
        verbose_name="Smiles",
        default="",
    )
    Score = models.FloatField(null=True)
    MOA = models.CharField(
        max_length=300,
        help_text="MOA",
        verbose_name="MOA",
        default="",
    )
    Investigation = models.CharField(
        max_length=300,
        help_text="Investigation",
        verbose_name="Investigation",
        default="",
    )
    ChemblID = models.CharField(
        max_length=300,
        help_text="ChemblID",
        verbose_name="ChemblID",
        default="",
    )
    Toxicity = models.CharField(
        max_length=300,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default="",
    )
    Drug_Name = models.CharField(
        max_length=2000,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default="",
    )
    clue_moa = models.CharField(
        max_length=300,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default="",
    )
    clinical_phase = models.CharField(
        max_length=300,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )
    Source = models.CharField(
        max_length=300,
        help_text="Source",
        verbose_name="Source",
        default="",
    )
    pref_name = models.CharField(
        max_length=300,
        help_text="pref_name",
        verbose_name="pref_name",
        default="",
    )
    Gene_Name = models.CharField(
        max_length=300,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )

# Parkinson's Disease
class D010300(models.Model):
    Uniprot = models.CharField(
        max_length=300,
        help_text="Uniprot",
        verbose_name="Uniprot",
        default="",
    )
    Smiles = models.CharField(
        max_length=2000,
        help_text="Smiles",
        verbose_name="Smiles",
        default="",
    )
    Score = models.FloatField(null=True)
    MOA = models.CharField(
        max_length=300,
        help_text="MOA",
        verbose_name="MOA",
        default="",
    )
    Investigation = models.CharField(
        max_length=300,
        help_text="Investigation",
        verbose_name="Investigation",
        default="",
    )
    ChemblID = models.CharField(
        max_length=300,
        help_text="ChemblID",
        verbose_name="ChemblID",
        default="",
    )
    Toxicity = models.CharField(
        max_length=300,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default="",
    )
    Drug_Name = models.CharField(
        max_length=2000,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default="",
    )
    clue_moa = models.CharField(
        max_length=300,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default="",
    )
    clinical_phase = models.CharField(
        max_length=300,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )
    Source = models.CharField(
        max_length=300,
        help_text="Source",
        verbose_name="Source",
        default="",
    )
    pref_name = models.CharField(
        max_length=300,
        help_text="pref_name",
        verbose_name="pref_name",
        default="",
    )
    Gene_Name = models.CharField(
        max_length=300,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )

# Pituitary Adenoma
class D049912(models.Model):
    Uniprot = models.CharField(
        max_length=300,
        help_text="Uniprot",
        verbose_name="Uniprot",
        default="",
    )
    Smiles = models.CharField(
        max_length=2000,
        help_text="Smiles",
        verbose_name="Smiles",
        default="",
    )
    Score = models.FloatField(null=True)
    MOA = models.CharField(
        max_length=300,
        help_text="MOA",
        verbose_name="MOA",
        default="",
    )
    Investigation = models.CharField(
        max_length=300,
        help_text="Investigation",
        verbose_name="Investigation",
        default="",
    )
    ChemblID = models.CharField(
        max_length=300,
        help_text="ChemblID",
        verbose_name="ChemblID",
        default="",
    )
    Toxicity = models.CharField(
        max_length=300,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default="",
    )
    Drug_Name = models.CharField(
        max_length=2000,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default="",
    )
    clue_moa = models.CharField(
        max_length=300,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default="",
    )
    clinical_phase = models.CharField(
        max_length=300,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )
    Source = models.CharField(
        max_length=300,
        help_text="Source",
        verbose_name="Source",
        default="",
    )
    pref_name = models.CharField(
        max_length=300,
        help_text="pref_name",
        verbose_name="pref_name",
        default="",
    )
    Gene_Name = models.CharField(
        max_length=300,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    
# MOA Status from TTD Database
class TTD_MOA_Status(models.Model):
    TargetID = models.CharField(
        max_length=200,
        help_text="Target ID",
        verbose_name="Target ID",
        default='',
    )
    DrugID = models.CharField(
        max_length=200,
        help_text="Drug ID",
        verbose_name="Drug ID",
        default='',
    )
    Highest_Status = models.CharField(
        max_length=200,
        help_text="Highest Status",
        verbose_name="Highest Status",
        default='',
    )
    MOA = models.CharField(
        max_length=200,
        help_text="MOA",
        verbose_name="MOA",
        default='',
    )
    Smiles_ID = models.CharField(
        max_length=2000,
        help_text="Smiles ID",
        verbose_name="Smiles ID",
        default='',
    )
    UniprotID = models.CharField(
        max_length=20,
        help_text="Uniprot ID",
        verbose_name="Uniprot ID",
        default='',
    )
    
# IC50 values from TTD
class TTD_IC50(models.Model):
    TargetID = models.CharField(
        max_length=20,
        help_text="Target ID",
        verbose_name="Target ID",
        default='',
    )
    DrugID = models.CharField(
        max_length=20,
        help_text="Drug ID",
        verbose_name="Drug ID",
        default='',
    )
    UniprotID = models.CharField(
        max_length=20,
        help_text="Uniprot ID",
        verbose_name="Uniprot ID",
        default='',
    )
    Smiles_ID = models.CharField(
        max_length=2000,
        help_text="Smiles ID",
        verbose_name="Smiles ID",
        default='',
    )
    Activity_IC50 = models.CharField(
        max_length=50,
        help_text="Activity IC50",
        verbose_name="Activity IC50",
        default='',
    )

# CLUE Database
class CLUE(models.Model):
    Chembl_ID = models.CharField(
        max_length=50,
        help_text="Chembl ID",
        verbose_name="Chembl ID",
        default='',
    ) 
    Smiles_ID = models.CharField(
        max_length=2000,
        help_text="Smiles ID",
        verbose_name="Smiles ID",
        default='',
    )
    Drug_Name = models.CharField(
        max_length=100,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default='',
    )
    Clinical_Phase = models.CharField(
        max_length=20,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default='',
    )
    MOA = models.CharField(
        max_length=200,
        help_text="MOA",
        verbose_name="MOA",
        default='',
    )
    UniprotID = models.CharField(
        max_length=200,
        help_text="Uniprot ID",
        verbose_name="Uniprot ID",
        default='',
    )

# Stitch Database
class Stitch(models.Model):
    Chemical_ID = models.CharField(
        max_length=50,
        help_text="Chemical ID",
        verbose_name="Chemical ID",
        default='',
    )
    Protein_ID = models.CharField(
        max_length=50,
        help_text="Protein ID",
        verbose_name="Protein ID",
        default='',
    ) 
    Combined_Score = models.FloatField(
        help_text="Combined Score",
        verbose_name="Combined Score",
        null=True
    )
    Smiles_ID = models.CharField(
        max_length=2000,
        help_text="Smiles ID",
        verbose_name="Smiles ID",
        default='',
    )
    UniprotID = models.CharField(
        max_length=200,
        help_text="Uniprot ID",
        verbose_name="Uniprot ID",
        default='',
    )

# Chembl Database
class Chembl(models.Model):
    Chembl_ID = models.CharField(
        max_length=50,
        help_text="Chembl ID",
        verbose_name="Chembl ID",
        default='',
    )
    UniprotID = models.CharField(
        max_length=200,
        help_text="Uniprot ID",
        verbose_name="Uniprot ID",
        default='',
    )
    Smiles_ID = models.CharField(
        max_length=2000,
        help_text="Smiles ID",
        verbose_name="Smiles ID",
        default='',
    )
    Investigation = models.CharField(
        max_length=100,
        help_text="Investigation",
        verbose_name="Investigation",
        default='',
    )	
    MOA	= models.CharField(
        max_length=200,
        help_text="TTD MOA",
        verbose_name="TTD MOA",
        default='',
    )
    Toxicity = models.CharField(
        max_length=500,
        help_text="Toxicity",
        verbose_name="Toxicity",
        default='',
    )	
    pIC50 = models.FloatField(null=True)	
    Clue_MOA = models.CharField(
        max_length=200,
        help_text="Clue MOA",
        verbose_name="Clue MOA",
        default='',
    )
    Clinical_Phase = models.CharField(
        max_length=200,
        help_text="Clinical Phase",
        verbose_name="Clinical Phase",
        default="",
    )

# Drug Names
class Drug_Names_Smiles(models.Model):
    Drug_Name = models.CharField(
        max_length=100,
        help_text="Drug Name",
        verbose_name="Drug Name",
        default='',
    )
    CNS = models.CharField(
        max_length=5,
        help_text="CNS Drug",
        verbose_name="CNS Drug",
        default='',
    )
    Smiles_ID = models.CharField(
        max_length=2000,
        help_text="Smiles ID",
        verbose_name="Smiles ID",
        default='',
    )

# Diseases for BDDF
class BDDF_Disease(models.Model):
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