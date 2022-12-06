from django.contrib import admin
from .models import Peptide, Protein, GeneProt, PhosphoPeptide
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# Import Export Configuration
class GeneProtResource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = GeneProt
        # Fields useful for import and export
        fields = ('id', 'protName', 'entryName','geneName', 'altGeneNames', 'geneProtFullNames','chromosome', 'protLength', 'protMass')
        # Fields which will be useful for object identification during import
        import_id_fields = ('id','protName')
        # This will allow to skip unchanged entries
        skip_unchanged = False
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class ProteinResource(resources.ModelResource):
    geneProt = fields.Field(
        column_name='geneProt',
        attribute='geneProt',
        widget=widgets.ForeignKeyWidget(GeneProt, 'protName'))

    class Meta:
        # Controls which Model this resource is for
        model = Protein
        # Fields useful for import and export
        fields = ('id', 'proteinId', 'geneProt','AMY_L_Med', 'AMY_R_Med', 'AMY_Med', 'BS_L_Med', 'BS_R_Med', 'BS_Med', 'CING_L_Med', 'CING_R_Med', 'CING_Med', 'CN_L_Med', 'CN_R_Med', 'CN_Med', 'CV_L_Med', 'CV_R_Med', 'CV_Med', 'DG_L_Med', 'DG_R_Med', 'DG_Med', 'FCM_L_Med', 'FCM_R_Med', 'FCM_Med', 'FWM_L_Med', 'FWM_R_Med', 'FWM_Med', 'HIP_L_Med', 'HIP_R_Med', 'HIP_Med', 'LE_L_Med', 'LE_R_Med', 'LE_Med', 'LI_L_Med', 'LI_R_Med', 'LI_Med', 'OB_L_Med', 'OB_R_Med', 'OB_Med', 'OC_L_Med', 'OC_R_Med', 'OC_Med', 'PC_L_Med', 'PC_R_Med', 'PC_Med', 'PONS_L_Med', 'PONS_R_Med', 'PONS_Med', 'PUT_L_Med', 'PUT_R_Med', 'PUT_Med', 'SN_L_Med', 'SN_R_Med', 'SN_Med', 'TC_L_Med', 'TC_R_Med', 'TC_Med', 'THAL_L_Med', 'THAL_R_Med', 'THAL_Med',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('id','proteinId')
        # This will allow to skip unchanged entries
        skip_unchanged = False
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class PhosphoPeptideResource(resources.ModelResource):
    geneProt = fields.Field(
        column_name='geneProt',
        attribute='geneProt',
        widget=widgets.ForeignKeyWidget(GeneProt, 'protName'))

    class Meta:
        # Controls which Model this resource is for
        model = PhosphoPeptide
        # Fields useful for import and export
        fields = ('id', 'peptideSequence', 'geneProt', 'length', 'missedCleavages', 'phosphoPos', 'phosphoAminoAcid', 'AMY_L_Phos', 'AMY_R_Phos', 'BS_L_Phos', 'BS_R_Phos', 'CN_L_Phos', 'CN_R_Phos', 'CV_L_Phos', 'CV_R_Phos', 'CING_L_Phos', 'CING_R_Phos', 'DG_L_Phos', 'DG_R_Phos', 'FC_L_Phos', 'FC_R_Phos', 'HIP_L_Phos', 'HIP_R_Phos', 'MC_L_Phos', 'MC_R_Phos', 'SN_L_Phos', 'SN_R_Phos', 'SC_L_Phos', 'SC_R_Phos', 'THAL_L_Phos', 'THAL_R_Phos', 'Phospho_LH_Average', 'Phospho_RH_Average',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('id','peptideSequence')
        # This will allow to skip unchanged entries
        skip_unchanged = False
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class PeptideResource(resources.ModelResource):
    geneProt = fields.Field(
        column_name='geneProt',
        attribute='geneProt',
        widget=widgets.ForeignKeyWidget(GeneProt, 'protName'))

    class Meta:
        # Controls which Model this resource is for
        model = Peptide
        # Fields useful for import and export
        fields = ('id', 'peptideSequence', 'geneProt', 'length', 'missedCleavages',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('id','peptideSequence')
        # This will allow to skip unchanged entries
        skip_unchanged = False
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

# Register your models here.
class PhosphoPeptideAdmin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = PhosphoPeptideResource

    list_display = ('id','peptideSequence',)
    search_fields = ['peptideSequence']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class PeptideAdmin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = PeptideResource

    list_display = ('id','peptideSequence',)
    search_fields = ['peptideSequence']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class ProteinAdmin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = ProteinResource

    list_display = ('id','proteinId',)
    search_fields = ['proteinId']

class GeneProtAdmin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = GeneProtResource

    #Standard Settings
    list_display = ('id','protName', 'geneName', 'entryName','chromosome', 'geneProtFullNames')
    list_filter = ("chromosome",)
    search_fields = ['protName', 'geneName', 'geneProtFullNames']


admin.site.register(Peptide, PeptideAdmin)
admin.site.register(PhosphoPeptide, PhosphoPeptideAdmin)
admin.site.register(Protein, ProteinAdmin)
admin.site.register(GeneProt, GeneProtAdmin)
#admin.site.register(GeneFullName)
