WorkloadName=Test
InstanceProfile=''
InstanceTypeWeb=t2.micro
InstanceTypeApp=t2.micro
KeyName=walab
TemplateFile=template.json
STACK=`basename $(PWD)`
SourceLocation=`curl https://checkip.amazonaws.com`/32

AWS=AWS_SHARED_CREDENTIALS_FILE=../../.aws/credentials aws --debug --output yaml

all: 
	@head -18 Makefile
	@$(AWS) iam get-user --output yaml || echo 'Fix AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY'
	
stack-summaries:
	$(AWS) cloudformation list-stacks --query StackSummaries[] 

describe-stacks:
	$(AWS) cloudformation describe-stacks --query Stacks[] 

describe-stack:
	$(AWS) cloudformation describe-stacks --stack-name $(STACK) 

describe-stack-events:
	$(AWS) cloudformation describe-stack-events --stack-name $(STACK) --output yaml 2>&1 | tee -a stack-events.log

list-stack-resources:
	$(AWS) cloudformation list-stack-resources --stack-name $(STACK) --output yaml

ec2: ec2.ids
	$(AWS) ec2 describe-instances --instance-ids `cat ec2.ids` --query "Reservations[].Instances[]"

ec2-state: ec2.ids
	$(AWS) ec2 describe-instances --instance-ids `cat ec2.ids` --query "Reservations[].Instances[].State"

ec2.ips: ec2.ids
	$(AWS) ec2 start-instances --instance-ids `cat ec2.ids`
	$(AWS) ec2 wait instance-running --instance-ids `cat ec2.ids`
	$(AWS) ec2 describe-instances --instance-ids `cat ec2.ids` --query "Reservations[].Instances[].PublicIpAddress" --output text | tee ec2.ips

ec2-stop: ec2.ids
	$(AWS) ec2 stop-instances --instance-ids `cat ec2.ids` 
	rm -f ec2.ips

ec2-ssh-1: ec2.ips
	$(AWS) ec2 wait instance-running --instance-ids `cat ec2.ids`
	ssh -i $(KeyName).pem ec2-user@`cut -f1 ec2.ips`

ec2-ssh-2: ec2.ips
	$(AWS) ec2 wait instance-running --instance-ids `cat ec2.ids`
	ssh -i $(KeyName).pem ec2-user@`cut -f2 ec2.ips`

ec2-ssh-3: ec2.ips
	$(AWS) ec2 wait instance-running --instance-ids `cat ec2.ids`
	ssh -i $(KeyName).pem ec2-user@`cut -f3 ec2.ips`

ec2-ssh-4: ec2.ips
	$(AWS) ec2 wait instance-running --instance-ids `cat ec2.ids`
	ssh -i $(KeyName).pem ec2-user@`cut -f4 ec2.ips`

deploy-stack:
	$(AWS) cloudformation deploy \
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

ec2.ids:
	$(AWS) cloudformation list-stack-resources --stack-name $(STACK) --query "StackResourceSummaries[?ResourceType == 'AWS::EC2::Instance'].PhysicalResourceId" --output text > ec2.ids

delete-stack:
	$(AWS) cloudformation delete-stack --stack-name $(STACK) --output yaml --debug 2>&1 | tee -a delete-stack.log
	rm -f ec2.ips ec2.ids
