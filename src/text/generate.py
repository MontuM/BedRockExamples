import boto3
import json
import pprint

bedrock = boto3.client(service_name='bedrock-runtime',region_name='ap-south-1')

titan_model_id = 'amazon.titan-text-express-v1'

titan_config = json.dumps({
    "inputText": "Tell me a story about a dragon",
    "textGenerationConfig": {
        "maxTokenCount": 4096,
        "stopSequences": [],
        "temperature": 0,
        "topP": 1
    }
})

response = bedrock.invoke_model(
    body=titan_config,
    modelId=titan_model_id,
    accept="application/json",
    contentType="application/json"
)

resopnse_body = json.loads(response.get('body').read())

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(resopnse_body.get('results'))