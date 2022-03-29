all:
	export $(cat .env)
	aws iam list-users --query Users[].UserName | grep '"walab-admin"' || make create-user-walab-admin
	aws iam list-groups --query Groups[].GroupName | grep '"walab-admin"' || make create-group-walab-admin

create-user-walab-admin: 
	aws iam create-user --user-name walab-admin 

delete-user-walab-admin: 
	aws iam delete-user --user-name walab-admin 

create-group-walab-admin: 
	aws iam create-group --group-name walab-admin 

delete-group-walab-admin: 
	aws iam delete-group --group-name walab-admin 
