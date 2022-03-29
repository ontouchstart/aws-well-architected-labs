bash: get-user
	bash
	
get-user: 
	export $(cat .env)
	aws iam get-user || echo 'Fix AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY'

