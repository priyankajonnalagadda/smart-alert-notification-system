import unittest
from unittest.mock import patch
import python.snsPublisher as sns_module

class TestSNSPublisher(unittest.TestCase):

    @patch("boto3.client")
    def test_publish_alert_success(self, mock_boto_client):
        mock_sns = mock_boto_client.return_value
        mock_sns.publish.return_value = {"MessageId": "mock-id-123"}

        test_event = {
            "service": "PaymentGateway",
            "severity": "CRITICAL",
            "message": "Mocked alert message"
        }

        result = sns_module.publish_alert(test_event)
        self.assertTrue(result)
        mock_sns.publish.assert_called_once()

    @patch("boto3.client")
    def test_publish_alert_failure(self, mock_boto_client):
        mock_sns = mock_boto_client.return_value
        mock_sns.publish.side_effect = Exception("SNS Error")

        test_event = {
            "service": "PaymentGateway",
            "severity": "CRITICAL",
            "message": "This should fail"
        }

        result = sns_module.publish_alert(test_event)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
