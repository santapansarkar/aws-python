import boto3
import logging
import argparse
import os

def eks_connect():
    try:
        eks = boto3.client('eks')
        logging.info('AWS EKS client connected from python SDK')
    except:
        logging.error('An error identified duirng connecting to EKS client using python SDK. Please check log for more details')

def log_level(**kwargs):
    try:
        logging.basicConfig(**kwargs)
        logging.info('Logging level finalised')
    except:
        logging.error('An error identified duirng log level configuration. Please use any of these - CRITICAL,ERROR,WARNING,INFO,DEBUG')




if __name__=='__main__':
    # Define the parser variable to equal argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="Provides translation between one source language and another of the same set of languages.")

    # Add each of the arguments using the parser.add_argument() method
    
    parser.add_argument(
    '--logfile',
    dest="filename",
    type=str,
    help="Enter the name of log file",
    required=True
    )
    
    parser.add_argument(
        '--loglevel',
        dest="level",
        type=str,
        help="select the logging level for application run. Possible values - CRITICAL,ERROR,WARNING,INFO,DEBUG",
        required=True
        )
    # This will inspect the command line, convert each argument to the appropriate type and then invoke the appropriate action.
    args = parser.parse_args()
    
    log_cfg = {
                'filename':'eks.log',
                'format':'%(asctime)s - %(process)d - %(levelname)s - %(message)s',
                'level':'INFO'      
              }    

    log_level(**log_cfg)
    eks_connect()
        