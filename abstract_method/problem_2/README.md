# 📦 Notification Sender - Factory Method Practice

## 🧠 Objective
Design a scalable notification system using the Factory Method pattern. The system should support multiple notification channels like **Email**, **SMS**, and **Push notifications**.

Each notification type may have:
- Unique formatting requirements
- Different delivery mechanisms
- Custom retry or logging behaviors


## 🛠️ Requirements

### Interface
Define a base `NotificationSender` interface with a method:

```python
send(self, recipient, message)
```

### Implement channel-specific classes:

- EmailSender
- SmsSender
- PushSender

Each should override send() with channel-specific logic.

### Factory Method Structure
Create an abstract `NotificationManager` class with a `notify()` method:

```python
def notify(self, recipient, message):
    sender = self.create_sender()
    sender.send(recipient, message)

@abstractmethod
def create_sender(self) -> NotificationSender:
    pass
```

Then implement concrete managers:

- EmailNotificationManager
- SmsNotificationManager
- PushNotificationManager

Each manager overrides `create_sender()` to return its corresponding sender.

## 🚀 Goals
- Decouple sender creation from business logic
- Allow easy extensibility for future channels
- Showcase clean usage of Factory Method principles

## 🧩 Bonus Challenges
- Add priority handling or batch sending
- Implement retry logic or fallback channels
- Include logging hooks for delivery status