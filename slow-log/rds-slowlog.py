#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import boto3

try:
    response = boto3.client('rds').describe_db_instances()
    x=','
    for r in response['DBInstances']:
        db_instance_name = r['DBInstanceIdentifier']
        db_engine =  r['Engine']
        print ( db_instance_name, x, db_engine )
except Exception as error:
    print (error)