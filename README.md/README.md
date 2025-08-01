 Smart Alert & Notification System

This project is a self-service alert and notification system built using **Groovy** and **Python**, integrated with **AWS SNS/SQS**. It simulates real-time alerts triggered by events and sends automated notifications using configuration-driven rules.

---

 Tech Stack

- **Groovy**  Scripted event trigger engine
- **Python**  AWS SNS publisher
- **AWS SNS/SQS**  Cloud messaging service
- **JSON**  Rule configuration
- **Unit Testing**  Python `unittest` + mocking
- **CI/CD Ready**  Can integrate with Jenkins or GitHub Actions

---

 Features

- Trigger alerts based on simulated events using Groovy
- Dynamic rule loading from `alert_rules.json`
- Publish alerts to AWS SNS topic using Python
- Modular structure for plug-and-play alert logic
- Includes test cases for core publishing logic

---

 Folder Structure

smart-alert-notification-system/
 groovy/
 alertTrigger.groovy
 python/
 snsPublisher.py
 config/
 alert_rules.json
 tests/
 test_snsPublisher.py
 README.md
 requirements.txt
 LICENSE

yaml
Copy
Edit

---

 Sample Flow

1. Groovy script simulates an event.
2. Event type is checked against rules in `alert_rules.json`.
3. If matched, Python publishes a message to SNS topic.
4. SNS notifies subscribed endpoints (email, Lambda, SQS, etc.).

---

 License

This project is licensed under the [MIT License](LICENSE).