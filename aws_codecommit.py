import boto3

client = boto3.client('codecommit')

if __name__ == '__main__':
    print('Hello from boto3')