import json
import argparse

def input_file(fname):
    with open(fname,'r') as json_file:
        json_content = json.load(json_file)
        json_formatted = json.dumps(json_content,indent=2)
        #print(type(json_formatted))
        repo_name = json_content['repositories'][0]['repositoryName']
        #print(f'repositoryName is {repo_name}')
        for rec in json_content['repositories']:
            #rec_formatted = json.dumps(rec, indent=2)
            #print(rec_formatted)
            for repo_name in rec:
                print(repo_name['repositoryName'])



if __name__=='__main__':
    input_file('ecr-describe-repositories.json')
