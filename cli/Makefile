# root level Makefile
# Make sure you have crendentials/config that allow admin in the .aws/credentials and .aws/config
#

AWS=AWS_SHARED_CREDENTIALS_FILE=.aws/credentials AWS_CONFIG_FILE=.aws/config aws

get-user:
	@$(AWS) iam get-user
