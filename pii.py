key = "e038d584b44c4f10a56421f2e0351bef"
endpont = "https://youtubenm1.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client():
    ta_credential = AzureKeyCredential(key=key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpont, credential=ta_credential)
    return text_analytics_client


client = authenticate_client()

documents = [
    "The employee's SSN is 859-98-0987",
    "The employee's phone number is 555-555-5555",
    "The employee's name is John Doe"
]

response = client.recognize_pii_entities(documents=documents,language="en")

result = [doc for doc in response if not doc.is_error]

for doc in result:
    print(f"Redacted Text {doc.redacted_text}")
    for entity in doc.entities:
        print(f"\t Category: {entity.category}")
        print(f"\t Condidence Score: {entity.confidence_score}")
        print(f"\t Entity: {entity.text}")