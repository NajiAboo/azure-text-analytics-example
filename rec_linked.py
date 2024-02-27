from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

key = "ea3954a901184dad95c74faf94d98f9f"
endpoint= "https://youtube1.cognitiveservices.azure.com/"

client = TextAnalyticsClient(endpoint=endpoint, credential = AzureKeyCredential(key))

documents = [
    """Microsoft was founded by Bill Gates with some friends he met at Harvard. One of his friends,
    Steve Ballmer, eventually became CEO after Bill Gates as well. Steve Ballmer eventually stepped
    down as CEO of Microsoft, and was succeeded by Satya Nadella.
    Microsoft originally moved its headquarters to Bellevue, Washington in January 1979, but is now
    headquartered in Redmond.

"""
]

result = client.recognize_linked_entities(documents)
docs = [ doc for doc in result if not doc.is_error]

for doc in docs:
    for entity in doc.entities:
        print(f" Entity : {entity.name}, its mentioned {len(entity.matches)} times")

        if entity.data_source == "Wikipedia":
            print(f"URL: {entity.url}")
    