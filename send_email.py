import json
import boto3


def lambda_handler(event, context):

    for i in event["Records"]:
        action = i["eventName"]
        ip = i["requestParameters"]["sourceIPAddress"]
        bucket_name = i["s3"]["bucket"]["name"]
        object = i["s3"]["object"]["key"]

    client = boto3.client("ses")

    subject = "New object received on {0} bucket".format(event['Records'][0]['s3']['bucket']['name'])
    body = """
        <br>
        This email is to notify you regarding {} event happened in bucket name {}
        The object {}
        Source IP: {}
        """.format(action, bucket_name, object, ip)

    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}

    response = client.send_email(
        Source="source email",
        Destination={"ToAddresses": ["email address of the person you are sending the email to"]},
        Message=message,
    )

    return "Thanks"
