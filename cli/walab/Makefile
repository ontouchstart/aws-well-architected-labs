NAME=`basename $(PWD)`
ADMIN_ARN=arn:aws:iam::aws:policy/AdministratorAccess

all: .aws
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam get-group --group-name $(NAME)-group
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam get-user --user-name $(NAME)-admin
	
.aws:
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam create-group --group-name $(NAME)-group
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam attach-group-policy --group-name $(NAME)-group --policy-arn $(ADMIN_ARN)
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam create-user --user-name $(NAME)-admin
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam add-user-to-group --user-name $(NAME)-admin --group-name $(NAME)-group
	mkdir .aws
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam get-user --user-name $(NAME)-admin
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam get-group --group-name $(NAME)-group

clean: 
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam remove-user-from-group --user-name $(NAME)-admin --group-name $(NAME)-group
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam delete-user --user-name $(NAME)-admin
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam detach-group-policy --group-name $(NAME)-group --policy-arn $(ADMIN_ARN)
	AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials AWS_CONFIG_FILE=../.aws/config aws iam delete-group --group-name $(NAME)-group
	rm -rf .aws
