import json
import argparse

def input_file(fname):
    with open(fname,'r') as json_file:
        json_content = json.load(json_file)
        json_formatted = json.dumps(json_content,indent=2)
        print(json_formatted)


if __name__=='__main__':
    input_file('ecr-describe-repositories.json')
