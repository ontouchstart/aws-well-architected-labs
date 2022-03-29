all:
	export $(cat .env)
	aws iam list-users --query Users[].UserName | grep '"walab-admin"' || make add-walab-admin

add-walab-admin: 
	aws iam create-user --user-name walab-admin 

delete-walab-admin: 
	aws iam delete-user --user-name walab-admin 

