# Send-email-notification-on-AWS-S3-events-via-Lambda-Function
This will show you how to trigger email notifications on s3 events via lambda function

Prerequisites
1. AWS account


If you do have an account, check the AWS services you will use below

1. You need to create an IAM Role for lambda access to s3 and SES
2. S3 bucket
3. Lambda function
4. SES (verify your email with Amazon SES)

ps: THIS TUTORIAL IS USING PYTHON!!


STEP 1

- Go to IAM
- Create a role and give it the following permissions 
  * AWSLambdaExecute
  * AmazonSESFullAccess
  * AmazonS3FullAccess

Once the role is created, go to step 2

STEP 2

- Go to lambda
- Click on create function
- Give your function a name
- Under Runtime, choose Python 3.8
- Click on the Change default execution role dropdown, then choose use existing role
- Under Existing role, choose the role you created in STEP 1
- Then click create function

Once you have created the function, go the step 3

STEP 3
- Create a bucket

Once you have create the bucket, go do the next steps
- Go to your bucket, click on Properties
- Scroll to Event notifications and click create event notification
- Give your event a name
- Under Event Types, click the checkbox All object create events
- Under Destination, choose lambda function
- Under Specify Lambda function, click on Choose from your Lambda functions
- Then on the dropdown, choose your existing lambda function from STEP 2
- Save changes


STEP 4
- Go to SES
- Create an identity
- Choose email address
- Type the email address 
- Create identity
Be on the lookout for the email that will ask you to verify your email and verify your email
To make sure that your email is verified, go to verified identities and check if Status is verified


After all of this is set up, go to your lambda function.
Use the tutorial provided to edit the code and deploy when you are done. Customise your message, subject and anything else to best suit your needs. Check the boto3 document here for reference https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.send_email


okay bye
