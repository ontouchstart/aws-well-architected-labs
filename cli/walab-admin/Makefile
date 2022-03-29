all: add-user-to-group-walab-admin
	export $(cat .env)
	aws iam get-group --group-name walab-admin
	aws iam list-attached-group-policies --group-name walab-admin
	bash

create-user-walab-admin: 
	export $(cat .env)
	aws iam list-users --query Users[].UserName | grep '"walab-admin"' || aws iam create-user --user-name walab-admin 

delete-user-walab-admin: delete-group-walab-admin
	export $(cat .env)
	aws iam delete-user --user-name walab-admin 

create-group-walab-admin: 
	export $(cat .env)
	aws iam list-groups --query Groups[].GroupName | grep '"walab-admin"' || aws iam create-group --group-name walab-admin 
	aws iam attach-group-policy --group-name walab-admin --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
	aws iam get-group --group-name walab-admin
	aws iam list-attached-group-policies --group-name walab-admin

add-user-to-group-walab-admin: create-user-walab-admin create-group-walab-admin
	export $(cat .env)
	aws iam add-user-to-group --user-name walab-admin --group-name walab-admin 
	aws iam get-group --group-name walab-admin

delete-group-walab-admin: 
	export $(cat .env)
	aws iam remove-user-from-group --user-name walab-admin --group-name walab-admin 
	aws iam detach-group-policy --group-name walab-admin --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
	aws iam delete-group --group-name walab-admin 

clean: delete-user-walab-admin
