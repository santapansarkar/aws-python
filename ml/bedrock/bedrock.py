import boto3,json

boto3.setup_default_session(profile_name='sxsarkar')

bedrock_runtime = boto3.client('bedrock-runtime')

prompt = input('Ask me anything : ')
print('well, well...you want to know this, fine...gimme sometime....')

#prompt = 'Write a story about school picnic'

kwargs = {
    "body" : "{\"prompt\":\"\\n\\nHuman:\\n\\n "+ prompt +"\\n\\nAssistant:\\n \",\"max_tokens_to_sample\":300,\"temperature\":1,\"top_k\":250,\"top_p\":0.999,\"stop_sequences\":[\"\\n\\nHuman:\"],\"anthropic_version\":\"bedrock-2023-05-31\"}",
    "contentType" : "application/json",
    "accept" : "application/json",
    "modelId" : 'anthropic.claude-v2'
}

response = bedrock_runtime.invoke_model(**kwargs)

response_body = json.loads(response.get('body').read())
completion = response_body.get('completion')
print(completion)