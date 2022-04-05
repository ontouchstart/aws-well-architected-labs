import boto3
iam = boto3.client('iam')
s3 = boto3.client('s3')
cf = boto3.client('cloudformation')
ec2 = boto3.client('ec2')

user = iam.get_user()
users = iam.list_users()
buckets = s3.list_buckets()
stacks = cf.list_stacks()
instances = ec2.describe_instances()

print(dir())
print(user)
