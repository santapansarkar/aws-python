import boto3
import json
import argparse


def translate_text(**kwargs):

    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText'])                                    

def input_payload():
    with open('translate-text.json') as fobj:
        json_content = json.load(fobj)
        for item in json_content['Input']:
            #print(item)
            translate_text(**item)



if __name__=='__main__':
    input_payload()