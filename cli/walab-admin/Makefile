all:
	export $(cat .env)
	aws iam list-users --query Users[].UserName | grep '"walab-admin"' || make create-user-walab-admin

create-user-walab-admin: 
	aws iam create-user --user-name walab-admin 

delete-user-walab-admin: 
	aws iam delete-user --user-name walab-admin 
