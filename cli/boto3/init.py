import boto3
import json
iam_client = boto3.client('iam')
s3_client = boto3.client('s3')
cf_client = boto3.client('cloudformation')
ec2_client = boto3.client('ec2')

user = iam_client.get_user()
users = iam_client.list_users()
buckets = s3_client.list_buckets()
stacks = cf_client.list_stacks()
instances = ec2_client.describe_instances()
vpcs = ec2_client.describe_vpcs()

print(dir())
print(json.dumps(user, indent=2, default=str))
print(json.dumps(instances, indent=2, default=str))
print(json.dumps(stacks, indent=2, default=str))
print(json.dumps(vpcs, indent=2, default=str))
