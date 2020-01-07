#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import boto3


def get_rds_arn():
    response = boto3.client('rds').describe_db_instances(Filters=[{'Name': 'engine', 'Values': ['mysql', 'mariadb', 'aurora-mysql']}])
    x = ','
    for r in response['DBInstances']:
        db_arn_list = r['DBInstanceArn']
        #return db_arn_list
        print(db_arn_list)


def main():
    get_rds_arn()


if __name__ == "__main__":
    main()


# aws resourcegroupstaggingapi get-resources --resource-type-filters rds:snapshot --tag-filters Key=blah


# try:
#     response = boto3.client('rds').describe_db_instances(Filters=[{'Name': 'engine', 'Values': ['mysql','mariadb','aurora-mysql']}])
#     x=','
#     for r in response['DBInstances']:
#         db_instance_arn = r['DBInstanceArn']
#         print( db_instance_arn )
# except Exception as error:
#     print (error)



# aws rds list-tags-for-resource --resource-name arn:aws:rds:us-east-1:803913471631:db:denise-dev-53 --filters "Name=expense_type,Values=R_and_D" --output text