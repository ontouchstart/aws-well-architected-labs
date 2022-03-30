all:
	aws iam get-user
	python3 get-user.py

instance-ids:
	aws ec2 describe-instances --query "Reservations[].Instances[].InstanceId"
	python3 instance-ids.py 

key-pairs:
	aws ec2 describe-key-pairs

versions:
	ssh -i $(PEM) ec2-user@$(EC2_IP1) cat /etc/os-release

