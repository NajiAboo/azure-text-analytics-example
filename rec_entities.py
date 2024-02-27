from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


key = "ea3954a901184dad95c74faf94d98f9f"
endpoint= "https://youtube1.cognitiveservices.azure.com/"

client = TextAnalyticsClient(endpoint=endpoint, credential = AzureKeyCredential(key))

document = [
    """
I, Naji Aboo, work at Triassic Solutions as a Data scientist in healthcare domain. Last day we had a team luch which cost aroud $1000.
This happend in India on 01-01-2024.

""",
""" 
 Azure AI services are the best in that category and its stated on November 2021
"""
]

result = client.recognize_entities(document)

print(result)

for idx, review in enumerate(result):
    for entity in review.entities:
        print(f"text: {entity.text}, category: {entity.category}, subcategory: {entity.subcategory}")

