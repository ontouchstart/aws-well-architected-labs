# Please run 
#
# export $(cat .env) 
#
# to set your environment 
#
# .env template
#
# AWS_ACCESS_KEY_ID=
# AWS_SECRET_ACCESS_KEY=
# AWS_DEFAULT_REGION=us-east-1
# WorkloadName=Test
# InstanceProfile=''
# InstanceTypeWeb=t2.micro
# InstanceTypeApp=t2.micro
# KeyName=walab
# SourceLocation=
# TemplateFile=OE_Inventory_and_Patch_Mgmt.json

all: 
	@head -18 Makefile
	@aws iam get-user --output yaml || echo 'Fix AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY'
	
stack-summaries:
	aws cloudformation list-stacks --query StackSummaries[] --output yaml

describe-stacks:
	aws cloudformation describe-stacks --query Stacks[] --output yaml

describe-stack:
	aws cloudformation describe-stacks --stack-name $(STACK) --output yaml

describe-stack-events:
	aws cloudformation describe-stack-events --stack-name $(STACK) --output yaml 2>&1 | tee -a stack-events.log

list-stack-resources:
	aws cloudformation list-stack-resources --stack-name $(STACK) --output yaml

# ec2
#
ec2:
	aws ec2 describe-instances --instance-ids `aws cloudformation list-stack-resources --stack-name $(STACK) --query "StackResourceSummaries[?ResourceType == 'AWS::EC2::Instance'].PhysicalResourceId"  --output text` --query "Reservations[].Instances[]" --output yaml


ec2-state:
	aws ec2 describe-instances --instance-ids `aws cloudformation list-stack-resources --stack-name $(STACK) --query "StackResourceSummaries[?ResourceType == 'AWS::EC2::Instance'].PhysicalResourceId"  --output text` --query "Reservations[].Instances[].State" --output yaml

ec2-ip:
	aws ec2 describe-instances --instance-ids `aws cloudformation list-stack-resources --stack-name $(STACK) --query "StackResourceSummaries[?ResourceType == 'AWS::EC2::Instance'].PhysicalResourceId"  --output text` --query "Reservations[].Instances[].PublicIpAddress" --output yaml

ec2-start:
	aws ec2 start-instances --instance-ids `aws cloudformation list-stack-resources --stack-name $(STACK) --query "StackResourceSummaries[?ResourceType == 'AWS::EC2::Instance'].PhysicalResourceId"  --output text` --output yaml 

ec2-stop:
	aws ec2 stop-instances --instance-ids `aws cloudformation list-stack-resources --stack-name $(STACK) --query "StackResourceSummaries[?ResourceType == 'AWS::EC2::Instance'].PhysicalResourceId"  --output text` --output yaml 

deploy-stack:
	aws cloudformation deploy \
		--stack-name $(STACK) \
		--template-file $(TemplateFile) \
		--parameter-overrides \
			WorkloadName=$(WorkloadName) \
			InstanceProfile=$(InstanceProfile) \
			InstanceTypeWeb=$(InstanceTypeWeb) \
			InstanceTypeApp=$(InstanceTypeApp) \
			KeyName=$(KeyName) \
			SourceLocation=$(SourceLocation) \
		--output yaml \
		--debug 2>&1 | tee -a deploy-stack.log

delete-stack:
	aws cloudformation delete-stack --stack-name $(STACK) --output yaml --debug 2>&1 | tee -a delete-stack.log
