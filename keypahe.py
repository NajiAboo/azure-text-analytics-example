key ="e038d584b44c4f10a56421f2e0351bef"
endpoint="https://youtubenm1.cognitiveservices.azure.com/"

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def auth_client():
    ta_credential = AzureKeyCredential(key=key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)
    return text_analytics_client


client = auth_client()

articles =[

     """
    Washington, D.C. Autumn in DC is a uniquely beautiful season. The leaves fall from the trees
    in a city chock-full of forests, leaving yellow leaves on the ground and a clearer view of the
    blue sky above...
    """,
    """
    Redmond, WA. In the past few days, Microsoft has decided to further postpone the start date of
    its United States workers, due to the pandemic that rages with no end in sight...
    """,
    """
    Redmond, WA. Employees at Microsoft can be excited about the new coffee shop that will open on campus
    once workers no longer have to work remotely...
    """
]



response = client.extract_key_phrases(documents=articles)

docs = [doc for doc in response if not doc.is_error]


for doc in docs:
    print(f" key phrases : { doc.key_phrases} ")