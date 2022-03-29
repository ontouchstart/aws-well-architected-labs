bash: get-caller-identity
	bash
	
get-caller-identity: 
	export $(cat .env)
	aws sts get-caller-identity || echo 'Fix AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY'

