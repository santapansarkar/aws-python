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

def repo_list():
    response = client.list_repositories()
    return response
def new_repo():
    response = client.create_repository(
        repositoryName='python-repo',
        repositoryDescription='This repository will hold aws workshop python source codes',
        )
def file_commit(**kwargs):
    response = client.put_file(
        repositoryName='string',
        branchName='string',
        fileContent=b'bytes',
        filePath='string',
        fileMode='EXECUTABLE' | 'NORMAL' | 'SYMLINK',
        parentCommitId='string',
        commitMessage='string',
        name='string',
        email='string'
    )
def new_branch(**kwargs):
    response = client.create_branch(
        repositoryName='string',
        branchName='string',
        commitId='string'
    )


if __name__ == '__main__':
    #new_repo()
    all_repo = repo_list()
    #print(type(all_repo))
    #print(all_repo['repositories'])
    for item in all_repo['repositories']:
        if item['repositoryName'] == 'python-repo':
            print(f'Finally we have a repository created for python source codes and repository id is {item["repositoryId"]}')

    input_new_branch = {
        'repositoryName':'python-repo',
        'branchName':'feature-codecommit',
        'commitId':'HEAD'
        }
    new_branch(**input_new_branch)
    #json_output = json.loads(all_repo)
    #print(json_output)



