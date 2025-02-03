from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

# Create your views here.

database = ["Bionda", "Harmonizome", "Pubpular", "Disgenet"]

disease_mapping = {
    "D000544": "Alzheimer's Disease",
    "D000690": "Amyotrophic Lateral Sclerosis",
    "D017204": "Angelman Syndrome",
    "D001008": "Anxiety Disorder",
    "D001037": "Aphasia",
    "D001260": "Ataxia Telangiectasia",
    "D001289": "Attention deficit hyperactivity disorder",
    "D000067877": "Autism Spectrum Disorder",
    "D001714": "Bipolar Disorder",
    "D002544": "Cerebral Infarction",
    "D002545": "Cerebral Ischemia",
    "D002547": "Cerebral Palsy",
    "D007562": "Creutzfeldt Jakob Disease",
    "D003704": "Dementia",
    "D004314": "Down Syndrome",
    "D004410": "Dyslexia",
    "D004421": "Dystonia",
    "D004660": "Encephalitis",
    "D004679": "Encephalomyelitis",
    "D004827": "Epilepsy",
    "D020329": "Essential Tremor",
    "D005600": "Fragile X Syndrome",
    "D005621": "Friedreich Ataxia",
    "D057180": "Frontotemporal Dementia",
    "D057174": "Frontotemporal Lobar Degeneration",
    "D005776": "Gaucher Disease",
    "D005879": "Gilles De La Tourette Syndrome",
    "D005909": "Glioblastoma",
    "D005910": "Glioma",
    "D006816": "Huntington's Disease",
    "D006849": "Hydrocephalus",
    "D008607": "Intellectual Disability",
    "D002532": "Intracranial Aneurysm",
    "D008527": "Medulloblastoma",
    "D008581": "Meningitis",
    "D008579": "Meningioma",
    "D016472": "Motor Neuron Disease",
    "D009103": "Multiple Sclerosis",
    "D009136": "Muscular Dystrophy",
    "D009290": "narcolepsy",
    "D009442": "Neurilemmoma",
    "D009447": "Neuroblastoma",
    "D018358": "Neuroendocrine Tumor",
    "D017253": "Neurofibromatosis",
    "D016584": "Panic Disorder",
    "D010235": "Paraganglioma",
    "D010300": "Parkinson's Disease",
    "D049912": "Pituitary Adenoma",
    "D018318": "Plexiform Neurofibroma",
    "D013313": "Post-traumatic Stress Disorder",
    "D011218": "Prader-Willi Syndrome",
    "D017096": "Prion Disease",
    "D015518": "Rett Syndrome",
    "D012559": "Schizophrenia",
    "D013661": "Tay-Sachs Disease",
    "D014402": "Tuberous Sclerosis",
}

disease_ID_list = [
    "D000544",
    "D000690",
    "D017204",
    "D001008",
    "D001037",
    "D001260",
    "D001289",
    "D000067877",
    "D001714",
    "D002544",
    "D002545",
    "D002547",
    "D007562",
    "D003704",
    "D004314",
    "D004410",
    "D004421",
    "D004660",
    "D004679",
    "D004827",
    "D020329",
    "D005600",
    "D005621",
    "D057180",
    "D057174",
    "D005776",
    "D005879",
    "D005909",
    "D005910",
    "D006816",
    "D006849",
    "D008607",
    "D002532",
    "D008527",
    "D008581",
    "D008579",
    "D016472",
    "D009103",
    "D009136",
    "D009290",
    "D009442",
    "D009447",
    "D018358",
    "D017253",
    "D016584",
    "D010235",
    "D010300",
    "D049912",
    "D018318",
    "D013313",
    "D011218",
    "D017096",
    "D015518",
    "D012559",
    "D013661",
    "D014402",
]

disease_list = [
    "Alzheimer's Disease",
    "Amyotrophic Lateral Sclerosis",
    "Angelman Syndrome",
    "Anxiety Disorder",
    "Aphasia",
    "Ataxia Telangiectasia",
    "Attention deficit hyperactivity disorder",
    "Autism Spectrum Disorder",
    "Bipolar Disorder",
    "Cerebral Infarction",
    "Cerebral Ischemia/Transient Cerebral Ischemia",
    "Cerebral Palsy",
    "Creutzfeldt Jakob Disease",
    "Dementia (Non-Alzheimer)",
    "Down Syndrome",
    "Dyslexia",
    "Dystonia",
    "Encephalitis",
    "Encephalomyelitis",
    "Epilepsy",
    "Essential Tremor",
    "Fragile X Syndrome",
    "Friedreich Ataxia",
    "Frontotemporal Dementia",
    "Frontotemporal Lobar Degeneration",
    "Gaucher Disease",
    "Gilles De La Tourette Syndrome",
    "Glioblastoma",
    "Glioma",
    "Huntington's Disease",
    "Hydrocephalus",
    "Intellectual Disability",
    "Intracranial Aneurysm",
    "Medulloblastoma",
    "Meningitis",
    "Meningioma",
    "Motor Neurone Disease",
    "Multiple Sclerosis",
    "Muscular Dystrophy",
    "narcolepsy",
    "Neurilemmoma",
    "Neuroblastoma",
    "Neuroendocrine Tumor",
    "Neurofibromatosis",
    "Panic Disorder",
    "Paraganglioma",
    "Parkinson's Disease",
    "Pituitary Adenoma",
    "Plexiform Neurofibroma",
    "Post-traumatic Stress Disorder",
    "Prader-Willi Syndrome",
    "Prion Disease",
    "Rett Syndrome",
    "Schizophrenia",
    "Tay-Sachs Disease",
    "Tuberous Sclerosis",
]


def get_all_objects(diseaseID, geneName):
	if diseaseID == "D000544":
		try:
			dataset = D000544.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D000544Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D000690":
		try:
			dataset = D000690.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D000690Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D017204":
		try:
			dataset = D017204.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D017204Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D001008":
		try:
			dataset = D001008.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D001008Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D001037":
		try:
			dataset = D001037.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D001037Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D001260":
		try:
			dataset = D001260.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D001260Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D001289":
		try:
			dataset = D001289.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D001289Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D000067877":
		try:
			dataset = D000067877.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D000067877Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D001714":
		try:
			dataset = D001714.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D001714Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D002544":
		try:
			dataset = D002544.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D002544Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D002545":
		try:
			dataset = D002545.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D002545Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D002547":
		try:
			dataset = D002547.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D002547Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D007562":
		try:
			dataset = D007562.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D007562Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D003704":
		try:
			dataset = D003704.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D003704Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D004314":
		try:
			dataset = D004314.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D004314Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D004410":
		try:
			dataset = D004410.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D004410Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D004421":
		try:
			dataset = D004421.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D004421Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D004660":
		try:
			dataset = D004660.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D004660Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D004679":
		try:
			dataset = D004679.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D004679Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D004827":
		try:
			dataset = D004827.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D004827Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D020329":
		try:
			dataset = D020329.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D020329Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D005600":
		try:
			dataset = D005600.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D005600Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D005621":
		try:
			dataset = D005621.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D005621Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D057180":
		try:
			dataset = D057180.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D057180Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D057174":
		try:
			dataset = D057174.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D057174Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D005776":
		try:
			dataset = D005776.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D005776Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D005879":
		try:
			dataset = D005879.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D005879Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D005909":
		try:
			dataset = D005909.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D005909Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D005910":
		try:
			dataset = D005910.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D005910Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D006816":
		try:
			dataset = D006816.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D006816Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D006849":
		try:
			dataset = D006849.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D006849Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D008607":
		try:
			dataset = D008607.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D008607Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D002532":
		try:
			dataset = D002532.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D002532Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D008527":
		try:
			dataset = D008527.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D008527Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D008581":
		try:
			dataset = D008581.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D008581Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D008579":
		try:
			dataset = D008579.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D008579Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D016472":
		try:
			dataset = D016472.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D016472Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D009103":
		try:
			dataset = D009103.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D009103Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D009136":
		try:
			dataset = D009136.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D009136Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D009290":
		try:
			dataset = D009290.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D009290Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D009442":
		try:
			dataset = D009442.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D009442Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D009447":
		try:
			dataset = D009447.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D009447Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D018358":
		try:
			dataset = D018358.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D018358Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D017253":
		try:
			dataset = D017253.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D017253Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D016584":
		try:
			dataset = D016584.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D016584Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D010235":
		try:
			dataset = D010235.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D010235Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D010300":
		try:
			dataset = D010300.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D010300Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D049912":
		try:
			dataset = D049912.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D049912Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D018318":
		try:
			dataset = D018318.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D018318Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D013313":
		try:
			dataset = D013313.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D013313Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D011218":
		try:
			dataset = D011218.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D011218Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D017096":
		try:
			dataset = D017096.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D017096Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D015518":
		try:
			dataset = D015518.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D015518Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D012559":
		try:
			dataset = D012559.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D012559Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D013661":
		try:
			dataset = D013661.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D013661Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)

	elif diseaseID == "D014402":
		try:
			dataset = D014402.objects.get(geneName=geneName)
		except:
			dataset = None
		serialized_dataset = D014402Serializer(dataset,fields=("geneName"),exclude=True,)
		return ({"scores": serialized_dataset.data},)


    
def get_all_genes(diseaseID):
	if diseaseID == "D000544":
		try:
			dataset = D000544.objects.all()
		except:
			dataset = None
		serialized_dataset = D000544Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D000690":
		try:
			dataset = D000690.objects.all()
		except:
			dataset = None
		serialized_dataset = D000690Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D017204":
		try:
			dataset = D017204.objects.all()
		except:
			dataset = None
		serialized_dataset = D017204Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D001008":
		try:
			dataset = D001008.objects.all()
		except:
			dataset = None
		serialized_dataset = D001008Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D001037":
		try:
			dataset = D001037.objects.all()
		except:
			dataset = None
		serialized_dataset = D001037Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D001260":
		try:
			dataset = D001260.objects.all()
		except:
			dataset = None
		serialized_dataset = D001260Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D001289":
		try:
			dataset = D001289.objects.all()
		except:
			dataset = None
		serialized_dataset = D001289Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D000067877":
		try:
			dataset = D000067877.objects.all()
		except:
			dataset = None
		serialized_dataset = D000067877Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D001714":
		try:
			dataset = D001714.objects.all()
		except:
			dataset = None
		serialized_dataset = D001714Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D002544":
		try:
			dataset = D002544.objects.all()
		except:
			dataset = None
		serialized_dataset = D002544Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D002545":
		try:
			dataset = D002545.objects.all()
		except:
			dataset = None
		serialized_dataset = D002545Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D002547":
		try:
			dataset = D002547.objects.all()
		except:
			dataset = None
		serialized_dataset = D002547Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D007562":
		try:
			dataset = D007562.objects.all()
		except:
			dataset = None
		serialized_dataset = D007562Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D003704":
		try:
			dataset = D003704.objects.all()
		except:
			dataset = None
		serialized_dataset = D003704Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D004314":
		try:
			dataset = D004314.objects.all()
		except:
			dataset = None
		serialized_dataset = D004314Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D004410":
		try:
			dataset = D004410.objects.all()
		except:
			dataset = None
		serialized_dataset = D004410Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D004421":
		try:
			dataset = D004421.objects.all()
		except:
			dataset = None
		serialized_dataset = D004421Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D004660":
		try:
			dataset = D004660.objects.all()
		except:
			dataset = None
		serialized_dataset = D004660Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D004679":
		try:
			dataset = D004679.objects.all()
		except:
			dataset = None
		serialized_dataset = D004679Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D004827":
		try:
			dataset = D004827.objects.all()
		except:
			dataset = None
		serialized_dataset = D004827Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D020329":
		try:
			dataset = D020329.objects.all()
		except:
			dataset = None
		serialized_dataset = D020329Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D005600":
		try:
			dataset = D005600.objects.all()
		except:
			dataset = None
		serialized_dataset = D005600Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D005621":
		try:
			dataset = D005621.objects.all()
		except:
			dataset = None
		serialized_dataset = D005621Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D057180":
		try:
			dataset = D057180.objects.all()
		except:
			dataset = None
		serialized_dataset = D057180Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D057174":
		try:
			dataset = D057174.objects.all()
		except:
			dataset = None
		serialized_dataset = D057174Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D005776":
		try:
			dataset = D005776.objects.all()
		except:
			dataset = None
		serialized_dataset = D005776Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D005879":
		try:
			dataset = D005879.objects.all()
		except:
			dataset = None
		serialized_dataset = D005879Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D005909":
		try:
			dataset = D005909.objects.all()
		except:
			dataset = None
		serialized_dataset = D005909Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D005910":
		try:
			dataset = D005910.objects.all()
		except:
			dataset = None
		serialized_dataset = D005910Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D006816":
		try:
			dataset = D006816.objects.all()
		except:
			dataset = None
		serialized_dataset = D006816Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D006849":
		try:
			dataset = D006849.objects.all()
		except:
			dataset = None
		serialized_dataset = D006849Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D008607":
		try:
			dataset = D008607.objects.all()
		except:
			dataset = None
		serialized_dataset = D008607Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D002532":
		try:
			dataset = D002532.objects.all()
		except:
			dataset = None
		serialized_dataset = D002532Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D008527":
		try:
			dataset = D008527.objects.all()
		except:
			dataset = None
		serialized_dataset = D008527Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D008581":
		try:
			dataset = D008581.objects.all()
		except:
			dataset = None
		serialized_dataset = D008581Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D008579":
		try:
			dataset = D008579.objects.all()
		except:
			dataset = None
		serialized_dataset = D008579Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D016472":
		try:
			dataset = D016472.objects.all()
		except:
			dataset = None
		serialized_dataset = D016472Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D009103":
		try:
			dataset = D009103.objects.all()
		except:
			dataset = None
		serialized_dataset = D009103Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D009136":
		try:
			dataset = D009136.objects.all()
		except:
			dataset = None
		serialized_dataset = D009136Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D009290":
		try:
			dataset = D009290.objects.all()
		except:
			dataset = None
		serialized_dataset = D009290Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D009442":
		try:
			dataset = D009442.objects.all()
		except:
			dataset = None
		serialized_dataset = D009442Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D009447":
		try:
			dataset = D009447.objects.all()
		except:
			dataset = None
		serialized_dataset = D009447Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D018358":
		try:
			dataset = D018358.objects.all()
		except:
			dataset = None
		serialized_dataset = D018358Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D017253":
		try:
			dataset = D017253.objects.all()
		except:
			dataset = None
		serialized_dataset = D017253Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D016584":
		try:
			dataset = D016584.objects.all()
		except:
			dataset = None
		serialized_dataset = D016584Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D010235":
		try:
			dataset = D010235.objects.all()
		except:
			dataset = None
		serialized_dataset = D010235Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D010300":
		try:
			dataset = D010300.objects.all()
		except:
			dataset = None
		serialized_dataset = D010300Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D049912":
		try:
			dataset = D049912.objects.all()
		except:
			dataset = None
		serialized_dataset = D049912Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D018318":
		try:
			dataset = D018318.objects.all()
		except:
			dataset = None
		serialized_dataset = D018318Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D013313":
		try:
			dataset = D013313.objects.all()
		except:
			dataset = None
		serialized_dataset = D013313Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D011218":
		try:
			dataset = D011218.objects.all()
		except:
			dataset = None
		serialized_dataset = D011218Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D017096":
		try:
			dataset = D017096.objects.all()
		except:
			dataset = None
		serialized_dataset = D017096Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D015518":
		try:
			dataset = D015518.objects.all()
		except:
			dataset = None
		serialized_dataset = D015518Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D012559":
		try:
			dataset = D012559.objects.all()
		except:
			dataset = None
		serialized_dataset = D012559Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D013661":
		try:
			dataset = D013661.objects.all()
		except:
			dataset = None
		serialized_dataset = D013661Serializer(dataset, many=True,)
		return serialized_dataset.data

	elif diseaseID == "D014402":
		try:
			dataset = D014402.objects.all()
		except:
			dataset = None
		serialized_dataset = D014402Serializer(dataset, many=True,)
		return serialized_dataset.data




@api_view(["GET"])
def single_gene_single_disease(request, geneName, diseaseID):
    geneName = geneName.upper()
    diseaseID = diseaseID.upper()
    if diseaseID in disease_ID_list:
        data = get_all_objects(diseaseID=diseaseID, geneName=geneName)
        disease = disease_mapping[diseaseID]
        return JsonResponse({"geneName": geneName, "disease": disease, "data": data})
    else:
        return JsonResponse(
            {
                "message": f'The diseaseID: "{diseaseID}" does not exist in BDMC Database or the query is malformed. Please refer to https://brainprot.org/api for help.'
            },
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["GET"])
def single_gene_all_data(request, geneName):
    data_list = []
    geneName = geneName.upper()
    for diseaseID in disease_ID_list:
        data = get_all_objects(diseaseID=diseaseID, geneName=geneName)
        disease = disease_mapping[diseaseID]
        data_list.append({"disease": disease, "diseaseData": data})
    return JsonResponse({"geneName": geneName, "data": data_list})


@api_view(["GET"])
def single_disease_all_gene(request, diseaseID):
    diseaseID = diseaseID.upper()
    if diseaseID in disease_ID_list:
        data = get_all_genes(diseaseID=diseaseID)
        disease = disease_mapping[diseaseID]
        return JsonResponse({"disease": disease, "geneList": data})
    else:
        return JsonResponse(
            {
                "message": f'The diseaseID: "{diseaseID}" does not exist in BDMC Database or the query is malformed. Please refer to https://brainprot.org/api for help.'
            },
            status=status.HTTP_404_NOT_FOUND,
        )
