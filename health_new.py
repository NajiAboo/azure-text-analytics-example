key="91ce96a8ce7c47258661c4a8cccb3176"
endpoint = "https://youtubenm1.cognitiveservices.azure.com/"

import os
import typing
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential= AzureKeyCredential(key=key)
)

documents = [
    """
  Patient needs to take 100 mg of ibuprofen and 3 mg of pottasium. also need to take 10 mg of Zocor
""",
"""
Patient needs to take 50mg of ibuprofen and 2 mg of coumadin.
"""
]



poller = client.begin_analyze_healthcare_entities(documents=documents)

resulst = poller.result()

docs = [ doc for doc in resulst if not doc.is_error]


for doc in docs:
    for entity in doc.entities:
        print(f"Entity: {entity.text}")
        print(f"... Normalzed text: {entity.normalized_text}")
        print(f"... Category: {entity.category}")
        if entity.data_sources is not None:
            for datasource in entity.data_sources:
                print(f"........... entityid : {datasource.entity_id}")
                print(f"........... name : {datasource.name}")
        
        if entity.assertion is not None:
            print(f"*********** Conditionality: {entity.assertion.conditionality}")


    for relation in doc.entity_relations:
        for role in relation.roles:
            print(f"Role . {role.name}  enity : {role.entity.text}")






