import boto3
import time
import logging


def describe_ec2():
    ec2 = boto3.client('ec2')
    logging.info("low level client object connected to AWS EC2")
    response = ec2.describe_instances()
    logging.info("Describe Instance API called")
    ec2_id = response['Reservations'][0]['Instances'][0]['InstanceId']
    logging.info(f'Details of ec2 instance id --> {ec2_id}')

    return ec2_id

def stop_ec2(instance_id):
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=[instance_id])    

def start_ec2(instance_id):
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=[instance_id], DryRun=False)

def describe_asg():
    asg = boto3.client('autoscaling')
    try:
         response = asg.describe_auto_scaling_groups()
         print(response)
    except Exception as e:
        raise e
        # TODO: write code...     
    
   

if __name__=='__main__':
    logging.basicConfig(filename='example.log',level=logging.INFO)
    #ec2_id = describe_ec2()    
    #stop_ec2(ec2_id)
    #time.sleep(10)
    #start_ec2(ec2_id)
    describe_asg()
    