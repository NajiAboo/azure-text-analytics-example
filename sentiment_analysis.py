import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


key = "ea3954a901184dad95c74faf94d98f9f"
endpoint= "https://youtube1.cognitiveservices.azure.com/"



text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential= AzureKeyCredential(key))

documents = [
    "I love to code",
    "I hate to sit idle",
    "I love to travel"
]


result = text_analytics_client.analyze_sentiment(documents, show_opinion_mining=True)

docs = [ doc for doc in result if not doc.is_error]

for idx, doc in enumerate(docs):
    print(f" Document Text : {documents[idx]}")
    print(f"overall sentiment: {doc.sentiment}")
