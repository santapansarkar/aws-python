import boto3

translate_client = boto3.client('translate')

#create a function to translate text from english to bengali using amazon translate
def translate_to_bengali():
    response = translate_client.translate_text(
    Text='Hello World',
    SourceLanguageCode='EN',
    TargetLanguageCode='BN',
    )
    print(type(response))
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print(response['TranslatedText'])
    else:
        print('Issue in translation')    

def list_translate_lang():
    response = translate_client.list_languages()
    for lang_header,lang_detail in response.items():
        #print(lang_header)
        #print(type(lang_detail))
        if lang_header == 'Languages':
            for lang_dict in lang_detail:
                for lang_key,lang_value in lang_dict.items():
                    if lang_key == 'LanguageName':
                        print(f"Code for {lang_value} language is : {lang_dict['LanguageCode']}")
    #print(type(response))


def main():
    #translate_to_bengali()
    list_translate_lang()

if __name__ == "__main__":
    main()


