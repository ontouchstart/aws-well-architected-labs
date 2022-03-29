bash: get-caller-identity
	bash
	
get-caller-identity: setenv
	aws sts get-caller-identity || echo 'Fix AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY'

setenv:
	-@export `cat .env`
