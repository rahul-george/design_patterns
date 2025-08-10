# 📦 Notification Sender - Factory Method Practice

## 🧠 Objective
Design a scalable notification system using the Factory Method pattern. The system should support multiple notification channels like **Email**, **SMS**, and **Push notifications**.

Each notification type may have:
- Unique formatting requirements
- Different delivery mechanisms
- Custom retry or logging behaviors

---

## 🛠️ Requirements

### Interface
Define a base `NotificationSender` interface with a method:

```python
send(self, recipient, message)
