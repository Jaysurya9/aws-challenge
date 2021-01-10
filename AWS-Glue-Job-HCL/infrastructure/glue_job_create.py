#!/usr/bin/env python

#Modules
import os
import sys
import json
import time
import boto3
import datetime


#Function
RETRIES = 3
ARGS = json.load(sys.stdin)
GLUE = boto3.client(
    service_name='glue',
    region_name=ARGS['aws_region'],
    endpoint_url='https://glue.{0}.amazonaws.com'.format(ARGS['aws_region']))

def main(retry_iterator=1):
    '''
    Trigger Glue JOB
    '''
    arguments = {
        "Name": ARGS['job_name'],
        "Role": ARGS['job_role'],
        "Command": {
            "Name": ARGS['job_script'],
            "ScriptLocation": ARGS['job_script_location']
        },
        "DefaultArguments": {
            "--TempDir": ARGS['job_tmp_dir'],
            "--job-bookmark-option": ARGS['job_bookmark_option'],
            "--job-language": ARGS['job_language']
        }
    }

    if ARGS['glue_connections_list']:
        arguments['Connections'] = {"Connections": ARGS['glue_connections_list'].split(',')}

    job_exist = False
    for i in GLUE.get_jobs()['Jobs']:
        if i['Name'] == ARGS['job_name']:
            job_exist = True
            result = "Job with this name existed"

    if job_exist is False:
        try:
            GLUE.create_job(**arguments)
            result = "Created"
        except Exception as exception:
            time.sleep(retry_iterator ** 2)
            if retry_iterator < RETRIES:
                return main(retry_iterator=retry_iterator + 1)
            raise Exception(exception)
    os.remove(ARGS['action_path'])
    return json.dumps({
        "JobName": ARGS['job_name'],
        "Result": result,
        "Retries": str(retry_iterator)
    })
#End Function
	
	
#Main
if __name__ == '__main__':
    if os.path.exists(ARGS['action_path']): print(main())
    else: print(json.dumps({'Action': 'Not Created'}))
#End Main
