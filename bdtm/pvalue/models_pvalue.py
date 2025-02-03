from django.db import models

# Create your models here.
class P_Value(models.Model):
    geneName = models.CharField(
        max_length=200,
        help_text="Gene Name",
        verbose_name="Gene Name",
        default="",
    )
    GSE43290 = models.FloatField(null = True)
    GSE54934 = models.FloatField(null = True)
    GSE62600 = models.FloatField(null = True)
    GSE12657 = models.FloatField(null = True)
    GSE13276 = models.FloatField(null = True)
    GSE36314 = models.FloatField(null = True)
    GSE13162 = models.FloatField(null = True)
    GSE83790_U133A = models.FloatField(null = True)
    GSE83790_U133B = models.FloatField(null = True)
    GSE20589 = models.FloatField(null = True)
    GSE19332 = models.FloatField(null = True)
    GSE68605 = models.FloatField(null = True)
    GSE52139 = models.FloatField(null = True)
    GSE83670 = models.FloatField(null = True)
    GSE38010 = models.FloatField(null = True)
    GSE5281 = models.FloatField(null = True)
    GSE48350 = models.FloatField(null = True)
    GSE1297 = models.FloatField(null = True)
    GSE4757 = models.FloatField(null = True)
    GSE12685 = models.FloatField(null = True)
    GSE16759 = models.FloatField(null = True)
    GSE28146 = models.FloatField(null = True)
    GSE8397_U133A = models.FloatField(null = True)
    GSE8397_U133B = models.FloatField(null = True)
    GSE7621 = models.FloatField(null = True)
    GSE19587 = models.FloatField(null = True)
    GSE20163 = models.FloatField(null = True)
    GSE20164 = models.FloatField(null = True)
    GSE20291 = models.FloatField(null = True)
    GSE20292 = models.FloatField(null = True)
    GSE20314 = models.FloatField(null = True)
    GSE20333 = models.FloatField(null = True)
    GSE24378 = models.FloatField(null = True)
    GSE20146 = models.FloatField(null = True)
    GSE20168 = models.FloatField(null = True)
    GSE20141 = models.FloatField(null = True)
