bash: get-user
	bash
	
get-user:
	aws iam get-user || echo 'Fix AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY'

validate:
	aws s3 ls $(S3)
	aws s3 cp $(S3) tmp
	cat tmp | jq .
	diff tmp OE_Inventory_and_Patch_Mgmt.json
	rm tmp
	aws cloudformation validate-template --template-url $(CFT)

describe-stacks:
	aws cloudformation describe-stacks --stack-name $(STACK)

describe-stack-events:
	aws cloudformation describe-stack-events --stack-name $(STACK)

ec2-ids:
	aws ec2 describe-instances --query Reservations[].Instances[].InstanceId

delete-stack:
	aws cloudformation delete-stack --stack-name $(STACK)
