# https://wellarchitectedlabs.com/well-architectedtool/200_labs/200_using_awscli_to_manage_wa_reviews/2_create_workload/

AWS=AWS_SHARED_CREDENTIALS_FILE=../.aws/credentials aws --debug --output yaml
NAME=`basename $(PWD)`

all:  ../.aws/credentials list-workloads.log
	cat list-workloads.log
	
list-workloads.log:
	$(AWS) wellarchitected create-workload --workload-name $(NAME) --description "Test Workload for WA Lab" --review-owner "John Smith" --environment "PRODUCTION" --aws-regions "us-east-1" --lenses "wellarchitected" "serverless"
	$(AWS) wellarchitected list-workloads --query "WorkloadSummaries[?WorkloadName == '$(NAME)'].WorkloadId" --output text | tee WorkloadId.log
	$(AWS) wellarchitected list-workloads | tee list-workloads.log

list-workload:
	$(AWS) wellarchitected list-workloads | tee list-workloads.log

clean:
	$(AWS) wellarchitected delete-workload --workload-id `cat WorkloadId.log`
	rm -f *.log
