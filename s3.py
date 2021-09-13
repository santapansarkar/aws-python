import boto3

def list_buckets():
    client = boto3.client('s3')
    response = client.list_buckets()
    for item in response['Buckets']:
        print(f"S3 bucket names - {item['Name']}")
        kwargs = {'Bucket':item['Name']} 
        #print(type(kwargs))
        list_objects(**kwargs)

def list_objects(**kwargs):
    client = boto3.client('s3')
    response = client.list_objects(**kwargs)
    object_struct = response['Contents']
    print('Objects inside buckets are below ')
    for rec in object_struct:
        print(rec['Key'])
    


if __name__=='__main__':
    list_buckets()