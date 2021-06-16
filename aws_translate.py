import boto3

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)

def file_reader():
    with open('aws_codecommit.py','r') as f:
        text = f.read()
        return text


### Change below this line only ###
if __name__=="__main__":
    input_text = file_reader()
    kwargs = {
                 'Text':input_text,
                'SourceLanguageCode':'en',
                'TargetLanguageCode':'de'
             }

    translate_text(**kwargs)

