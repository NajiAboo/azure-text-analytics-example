import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

key = "ea3954a901184dad95c74faf94d98f9f"
endpoint= "https://youtube1.cognitiveservices.azure.com/"

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential= AzureKeyCredential(key))

documents = [
    "Please subscribe my youtube channel",
    "Por favor subscribete a mi canal",
    "يرجى الاشتراك في قناتي",
    "ದಯವಿಟ್ಟು ನನ್ನ ಚಾನಲ್‌ಗೆ ಚಂದಾದಾರರಾಗಿ"
]

result = text_analytics_client.detect_language(documents)

docs = [ doc for doc in result if not doc.is_error]

for idx, doc in enumerate(docs):
    print(f"index: {idx}, language : {doc.primary_language.name}")