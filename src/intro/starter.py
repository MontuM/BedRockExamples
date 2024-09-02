import boto3
import pprint

bedrock = boto3.client(service_name='bedrock',region_name='ap-south-1')
pp = pprint.PrettyPrinter(depth=4)

def get_foundation_model(modelIdentifier):
    model = bedrock.get_foundation_model(modelIdentifier=modelIdentifier)
    pp.pprint(model)

def list_foundation_models(bedrock, pp):
    models = bedrock.list_foundation_models()
    for model in models["modelSummaries"]:
        get_foundation_model(model["modelId"])
        pp.pprint("--------------------------------------")
        

list_foundation_models(bedrock, pp)


