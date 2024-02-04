import boto3

translate_client = boto3.client('translate')

def validate_input_text(**kwargs):
    """Pre-Hook to validate the input text
    """
    support_lang = list_languages()
    try:
        if kwargs['Text'].lower() == 'restricted':
            print('Text cannot be translated as this is an restricted text')
        elif kwargs['TargetLanguageCode'] not in support_lang:
            print('Target language code is not supported')
        else:    
            translate_validated_text(**kwargs)
    except Exception as e:
        raise e
        
    
def translate_validated_text(**kwargs):
    """Translate text from source to target language
    """
    try:
        response = translate_client.translate_text(**kwargs)
        print(response['TranslatedText']) 
    except Exception as e:
        raise e    
    
def list_languages():
    """List all supported languages
    """
    try:
        response = translate_client.list_languages()
        for lang_code in response['Languages']:
            lang_list = lang_code['LanguageCode']
        return lang_list    
    except Exception as e:
        raise e    

    
    