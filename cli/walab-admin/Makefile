all: 
	aws iam get-user
	python3 get-user.py

list: add-user-to-group-walab-admin
	aws iam get-group --group-name walab-admin
	aws iam list-attached-group-policies --group-name walab-admin
	aws iam list-user-tags --user-name walab-admin
	bash

create-user-walab-admin: 
	aws iam list-users --query Users[].UserName | grep '"walab-admin"' || aws iam create-user --user-name walab-admin 
	aws iam tag-user --user-name walab-admin --tags Key=ROLE,Value=Administrator

delete-user-walab-admin: delete-group-walab-admin
	aws iam untag-user --user-name walab-admin --tag-keys ROLE
	aws iam delete-
	aws iam delete-user --user-name walab-admin 

create-group-walab-admin: 
	aws iam list-groups --query Groups[].GroupName | grep '"walab-admin"' || aws iam create-group --group-name walab-admin 
	aws iam attach-group-policy --group-name walab-admin --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
	aws iam get-group --group-name walab-admin
	aws iam list-attached-group-policies --group-name walab-admin

add-user-to-group-walab-admin: create-user-walab-admin create-group-walab-admin
	aws iam add-user-to-group --user-name walab-admin --group-name walab-admin 
	aws iam get-group --group-name walab-admin

delete-group-walab-admin: 
	aws iam remove-user-from-group --user-name walab-admin --group-name walab-admin 
	aws iam detach-group-policy --group-name walab-admin --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
	aws iam delete-group --group-name walab-admin 

clean: delete-user-walab-admin

######################
## Notes
######################
# aws iam create-login-profile --user-name walab-admin --password *****
# aws iam update-login-profile --user-name walab-admin --password ****

### Generate password with python
# python3
# Python 3.9.10 (main, Jan 15 2022, 11:48:00) 
# [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import secrets
# >>> secrets.token_urlsafe(32)
# '********************************'
