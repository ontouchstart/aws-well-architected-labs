NAME=`basename $(PWD)`
ADMIN_ARN=arn:aws:iam::aws:policy/AdministratorAccess
AWS=AWS_SHARED_CREDENTIALS_FILE=.aws/credentials aws --debug --output yaml
ROOT_AWS=AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials aws --debug --output yaml

all:  .aws/credentials
	$(AWS) iam get-group --group-name $(NAME)-group
	$(AWS) iam get-user --user-name $(NAME)-admin
	
.aws:
	$(ROOT_AWS) iam create-group --group-name $(NAME)-group
	$(ROOT_AWS) iam attach-group-policy --group-name $(NAME)-group --policy-arn $(ADMIN_ARN)
	$(ROOT_AWS) iam create-user --user-name $(NAME)-admin
	$(ROOT_AWS) iam add-user-to-group --user-name $(NAME)-admin --group-name $(NAME)-group
	mkdir .aws

.admin.key:
	$(ROOT_AWS) iam create-access-key --user-name $(NAME)-admin --output text > .admin.key

.aws/credentials: .aws .admin.key 
	echo '[default]' > .aws/credentials && echo 'aws_access_key_id='`cut -f2 .admin.key` >> .aws/credentials && echo 'aws_secret_access_key='`cut -f4 .admin.key` >> .aws/credentials
	sleep 10

remove-user-from-group: 
	$(ROOT_AWS) iam remove-user-from-group --user-name $(NAME)-admin --group-name $(NAME)-group

delete-access-key: 
	$(ROOT_AWS) iam delete-access-key --access-key-id  `cut -f2 .admin.key` --user-name $(NAME)-admin

delete-user:
	$(ROOT_AWS) iam delete-user --user-name $(NAME)-admin

delete-group:
	$(ROOT_AWS) iam detach-group-policy --group-name $(NAME)-group --policy-arn $(ADMIN_ARN)
	$(ROOT_AWS) iam delete-group --group-name $(NAME)-group

clean: remove-user-from-group delete-access-key delete-user delete-group 
	rm -rf .aws .admin.key
