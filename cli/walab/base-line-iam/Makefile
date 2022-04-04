TemplateFile=template.yaml
STACK=`basename $(PWD)`
AWS=AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials aws --debug --output yaml

all: stack-resources.log
	cat stack-resources.log
	
describe-stack:
	$(AWS) cloudformation describe-stacks --stack-name $(STACK)

describe-stack-events:
	$(AWS) cloudformation describe-stack-events --stack-name $(STACK)

stack-resources.log:
	$(AWS) cloudformation deploy \
		--stack-name $(STACK) \
		--capabilities CAPABILITY_NAMED_IAM \
		--template-file $(TemplateFile) \
		--debug 2>&1 | tee -a deploy-stack.log
	$(AWS) cloudformation list-stack-resources --stack-name $(STACK)  | tee stack-resources.log

clean:
	$(AWS) cloudformation delete-stack --stack-name $(STACK)
	rm -f *.log
