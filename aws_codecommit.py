import boto3
import json

client = boto3.client('codecommit')


def create_branch(**kwargs):
    response = client.create_branch(**kwargs)


def repolist_codecommit():
    """
    Identify the list of available repositories from AWS Code Commit and Choose the desired one
    :return:
    """
    response = client.list_repositories()
    nest_response = (response['repositories'])
    dict_response = nest_response[0]
    final_response = dict_response['repositoryName']
    return final_response


if __name__ == '__main__':
    print('Hello from boto3')
    repo_name = repolist_codecommit()
    input = {'repositoryName': repo_name,
             'branchName': 'pycharm',
             'commitId': '74928eae86d10249b892ec9f04d7b7e9d481ff5c'
             }
    create_branch(**input)

