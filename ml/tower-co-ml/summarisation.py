import boto3,json
boto3.setup_default_session(profile_name='sxsarkar')
bedrock_client = boto3.client('bedrock-runtime')

def prep_request():
    prompt = "Write me about planet foo"
    kwargs = {
        "body" : "{\"prompt\":\"\\n\\nHuman:\\n\\n "+ prompt +"\\n\\nAssistant:\\n \",\"max_tokens_to_sample\":300,\"temperature\":1,\"top_k\":250,\"top_p\":0.999,\"stop_sequences\":[\"\\n\\nHuman:\"],\"anthropic_version\":\"bedrock-2023-05-31\"}",
        "contentType" : "application/json",
        "accept" : "application/json",
        "modelId" : 'anthropic.claude-v2'
    }
    return kwargs

def invoke_llm():
    req_payload = prep_request()
    response = bedrock_client.invoke_model(**req_payload)
    response_body = json.loads(response.get('body').read())
    completion = response_body.get('completion')
    print(completion)
    return completion


