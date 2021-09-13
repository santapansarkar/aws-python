import boto3
import argparse

from botocore import parsers


def translate_data(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    http_out = response['ResponseMetadata']['HTTPStatusCode']
    if http_out == 200:
        print(response['TranslatedText'])
    else:
        print(response['TranslatedText method error'])

def aws_docker_registry():
    client = boto3.client('ecr')
    response = client.describe_registry()
    http_out = response['ResponseMetadata']['HTTPStatusCode']
    if http_out == 200:
        registry_input = {
                            'registryId' : (response['registryId'])
                         }  
        repository = client.describe_repositories(**registry_input)
        http_out = response['ResponseMetadata']['HTTPStatusCode']
        if http_out == 200:
            print(repository['repositories'][0]['repositoryName'])
            print(repository['repositories'][1]['repositoryName'])
        else:
            print(['describe_repositories method error'])
    else:
        print(response['describe_registry method error'])
    registry_id = input('Please provide private docker registry id:\t ')    
    repository_name = input('Please provide private docker repository name:\t ')
    image_input = {
                     'registryId' : registry_id,
                     'repositoryName' : repository_name   
                  } 
    image_details = client.list_images(**image_input)    
    print (f'Image tag is {image_details["imageIds"][0]["imageTag"]}')   


def cli_args():
    parser = argparse.ArgumentParser(description="fetch details of docker images")
    parser.add_argument(
                            '--registryId',
                            dest="registryId",
                            type=str,
                            help="The Amazon Web Services account ID associated with the registry that contains the repository in which to describe images. If you do not specify a registry, the default registry is assumed",
                            required=True
                       )
    parser.add_argument(
                            '--repositoryName',
                            dest="repositoryName",
                            type=str,
                            help="he repository that contains the images to describe.",
                            required=True
                        )

    args = parser.parse_args()

    client = boto3.client('ecr')

    response = client.describe_images(**vars(args))

    print(response)

def external_file(file):
    with open(file,'r') as f:
        text = f.read()
        print(text)





if __name__=="__main__":
    input_data = {
                    'Text':'I am learning python coding in AWS',
                    'SourceLanguageCode' : 'en',
                    'TargetLanguageCode' : 'beng'
                 }
    #translate_data(**input_data)
    

    #aws_docker_registry()
    #cli_args()
    external_file('wordpress.json')

