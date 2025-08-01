import boto3
import json

# Load AWS config (normally you'd use environment variables or AWS credentials config)
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:YourTopicName"

def publish_alert(event):
    client = boto3.client("sns", region_name="us-east-1")

    try:
        message = json.dumps(event)
        response = client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="Smart Alert Notification"
        )
        print(f"Alert published to SNS. Message ID: {response['MessageId']}")
        return True
    except Exception as e:
        print(f"Failed to publish alert: {str(e)}")
        return False

# Example: standalone test
if __name__ == "__main__":
    test_event = {
        "service": "PaymentGateway",
        "severity": "CRITICAL",
        "message": "Transaction failure rate exceeded threshold"
    }
    publish_alert(test_event)
