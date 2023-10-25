import boto3
import argparse


comprehend_client = boto3.client('comprehend')

def identify_lang():
    response = comprehend_client.batch_detect_dominant_language(
    TextList=[
        'string',
    ]
    )
    print(response)
    print(type(response))
    #json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)

def main():
    identify_lang()


if __name__ == "__main__":
    main()

