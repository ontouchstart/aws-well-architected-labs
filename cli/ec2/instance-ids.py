import boto3
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()
reservations = instances['Reservations']
for r in reservations:
	for i in r['Instances']:
		print(i['InstanceId'])
