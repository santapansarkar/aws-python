from copy import Error
import boto3
import logging
import argparse



def describe_ec2():
    try:
        ec2 = boto3.client('ec2')
        logging.info("low level client object connected to AWS EC2")
        response = ec2.describe_instances()
        logging.info("Describe Instance API called")
        ec2_id = response['Reservations'][0]['Instances'][0]['InstanceId']
        logging.info(f'Details of ec2 instance id --> {ec2_id}')
        return ec2_id
    except Exception as e:
        logging.error('issue in describing ec2 instances'.format(e))    

    

def stop_ec2(instance_id):
    try:
        ec2 = boto3.client('ec2')
        ec2.stop_instances(InstanceIds=[instance_id])    
    except Exception as e:
        logging.error('issue while stopping ec2'.format(e))
            

def start_ec2(instance_id):
    try:
        ec2 = boto3.client('ec2')
        ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
    except Exception as e:
        logging.error('issue while starting ec2'.format(e))



def describe_asg():
    try:
        asg = boto3.client('autoscaling')
        response = asg.describe_auto_scaling_groups()
        '''
        asg_name1 = response['AutoScalingGroups'][0]['AutoScalingGroupName']
        asg_name2 = response['AutoScalingGroups'][1]['AutoScalingGroupName']
        print(asg_name1, asg_name2)
        '''
        for rec in response['AutoScalingGroups']:
            logging.info(f"Auto scaling group names -> {rec['AutoScalingGroupName']}")
            #return rec['AutoScalingGroupName']
    except Exception as e:
        logging.error('issue while decsrbing asg'.format(e))

def scale_in_out(**kwargs):
    try:
        asg = boto3.client('autoscaling')
        response = asg.set_desired_capacity(**kwargs)  
        logging.info(f'desired capacity updated successfully for auto scaling group {args._get_args}')      
    except Exception as e:
        logging.error('Error while scale in/out activity'.format(e))    
    

def log_level(**kwargs):
    try:
        logging.basicConfig(**kwargs)
        logging.info('Logging level finalised')
    except:
        logging.error('An error identified duirng log level configuration. Please use any of these - CRITICAL,ERROR,WARNING,INFO,DEBUG')

    
   

if __name__=='__main__':
    log_cfg = {
            'filename':'ec2.log',
            'format':'%(asctime)s - %(process)d - %(levelname)s - %(message)s',
            'level':'INFO'      
            }    
    parser = argparse.ArgumentParser(description="Choose method of operation")

    # Add each of the arguments using the parser.add_argument() method
    parser.add_argument(
    '--opsname',
    dest="FunctionName",
    type=str,
    help="Enter Operation Name among these - stop_ec2,start_ec2,describe_asg,scale_in_out",
    required=True
    )
    
    # This will inspect the command line, convert each argument to the appropriate type and then invoke the appropriate action.
    args = parser.parse_args()
    input = {**vars(args)}
    if input['FunctionName'] == 'stop_ec2':
        print('call stop_ec2')
        #stop_ec2(ec2_id)
    elif input['FunctionName'] == 'start_ec2':
        print('call start_ec2')
        #start_ec2(ec2_id)
    elif input['FunctionName'] == 'describe_asg':
        print('call describe_asg')
        #describe_asg()
    elif input['FunctionName'] == 'scale_in_out':
        subparsers = parser.add_subparsers()
        #parser = argparse.ArgumentParser(description="Provides scaling capability of auto scaling group")
        # Add each of the arguments using the parser.add_argument() method
        subparse = subparsers.add_parser('opsname')
        subparse.add_argument(
        '--asgname',
        dest="AutoScalingGroupName",
        type=str,
        help="Enter Auto Scaling Group Name",
        required=True
        )
        subparse.add_argument(
            '--capacity',
            dest="DesiredCapacity",
            type=int,
            help="Provide desired compute value",
            required=True
            )
        # This will inspect the command line, convert each argument to the appropriate type and then invoke the appropriate action.
        args = subparse.parse_args()
        scale_in_out(**vars(args))        
        #print('call scale_in_out')
    else:
        print(input['FunctionName']) 



    

    #log_level(**log_cfg)
    #ec2_id = describe_ec2()    
    #stop_ec2(ec2_id)
    #start_ec2(ec2_id)
    #describe_asg()
    #scale_in_out()
   