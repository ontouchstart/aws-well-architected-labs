USER_NAME=`basename $(PWD)`

all: .aws
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam get-user --user-name $(USER_NAME)
	
.aws:
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam create-user --user-name $(USER_NAME)
	mkdir .aws
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam get-user --user-name $(USER_NAME)

clean: 
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam get-user --user-name $(USER_NAME)
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam delete-user --user-name $(USER_NAME)
	rm -rf .aws
