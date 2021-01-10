#!/usr/bin/env python

#Modules
import sys
import json
import time
import boto3


#Destroy Function
JOB = sys.argv[1]
REGION = sys.argv[2]
GLUE = boto3.client(
    service_name='glue',
    region_name=REGION ,
    endpoint_url='https://glue.{0}.amazonaws.com'.format(REGION))


def main():
    try:
        GLUE.delete_job(
            JobName=JOB
        )
        result = "Deleted"
    except:
        result = "Not Found"

    return json.dumps({
        "JobName": JOB,
        "Result": result
    }) #End Function

	
#Main	
if __name__ == '__main__':
    main()
#End
