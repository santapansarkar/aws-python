#create a simple webpage 
from flask import Flask, render_template, request
import boto3,json
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        ask = request.form.get('ask')
        response = invoke_llm(ask)
        return render_template('index.html', response=response)

    return render_template('index.html', text="**********AI Companion*********")

def invoke_llm(prompt):
    boto3.setup_default_session(profile_name='sxsarkar')
    bedrock_runtime = boto3.client('bedrock-runtime')
    #prompt = input('Ask me anything : ')
    #print('well, well...you want to know this, fine...gimme sometime....')

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
    
    #display completion into webpage
    return completion
    

if __name__ == "__main__":
    app.run(debug=True)