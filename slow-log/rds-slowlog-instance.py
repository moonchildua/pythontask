#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import boto3

try:
    response = boto3.client('rds').describe_db_instances(Filters=[{'Name': 'engine', 'Values': ['mysql','mariadb','aurora-mysql']}])
    x=','
    for r in response['DBInstances']:
        # db_instance_name = r['DBInstanceIdentifier']
        # db_engine =  r['Engine']
        db_instance_arn = r['DBInstanceArn']
        # print ( db_instance_name, x, db_engine, x, db_instance_arn )
        print( db_instance_arn )

except Exception as error:
    print (error)



# aws rds list-tags-for-resource --resource-name arn:aws:rds:us-east-1:803913471631:db:denise-dev-53 --filters "Name=expense_type,Values=R_and_D" --output text