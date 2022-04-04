WorkloadName=Test
InstanceProfile=''
InstanceTypeWeb=t2.micro
InstanceTypeApp=t2.micro
KeyName=walab
TemplateFile=template.json
STACK=`basename $(PWD)`
SourceLocation=`curl -sL https://checkip.amazonaws.com`/32

AWS=AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials aws --debug --output yaml

all: stack-resources.log
	cat stack-resources.log
	
ec2: ec2.ids
	$(AWS) ec2 describe-instances --instance-ids `cat ec2.ids` --query "Reservations[].Instances[]"

ec2-state: ec2.ids
	$(AWS) ec2 describe-instances --instance-ids `cat ec2.ids` --query "Reservations[].Instances[].State"

ec2-ids.log:	stack-resources.log
	$(AWS) cloudformation list-stack-resources --stack-name $(STACK) --query "StackResourceSummaries[?ResourceType == 'AWS::EC2::Instance'].PhysicalResourceId" --output text > ec2-ids.log

ec2-ips.log: ec2-ids.log
	$(AWS) ec2 start-instances --instance-ids `cat ec2-ids.log`
	$(AWS) ec2 wait instance-running --instance-ids `cat ec2-ids.log`
	$(AWS) ec2 describe-instances --instance-ids `cat ec2-ids.log` --query "Reservations[].Instances[].PublicIpAddress" --output text | tee ec2-ips.log

ec2-stop: ec2-ids.log
	$(AWS) ec2 stop-instances --instance-ids `cat ec2-ids.log` 
	rm -f ec2.ips

ec2-ssh-1: ec2-ips.log
	$(AWS) ec2 wait instance-running --instance-ids `cat ec2-ids.log`
	ssh -i $(KeyName).pem ec2-user@`cut -f1 ec2-ips.log`

ec2-ssh-2: ec2-ips.log
	$(AWS) ec2 wait instance-running --instance-ids `cat ec2-ids.log`
	ssh -i $(KeyName).pem ec2-user@`cut -f2 ec2-ips.log`

ec2-ssh-3: ec2-ips.log
	$(AWS) ec2 wait instance-running --instance-ids `cat ec2-ids.log`
	ssh -i $(KeyName).pem ec2-user@`cut -f3 ec2-ips.log`

ec2-ssh-4: ec2-ips.log
	$(AWS) ec2 wait instance-running --instance-ids `cat ec2-ids.log`
	ssh -i $(KeyName).pem ec2-user@`cut -f4 ec2-ips.log`

stack-resources.log:
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
	$(AWS) cloudformation list-stack-resources --stack-name $(STACK) | tee stack-resources.log


clean:
	$(AWS) cloudformation delete-stack --stack-name $(STACK) 
	rm -f *.log
