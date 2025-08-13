from abc import ABC, abstractmethod

# ------ Sender classes responsible for sending the SMS. ---------

class NotificationSenderError(Exception):
    pass

class RetryFailedError(Exception):
    pass

class NotificationSender(ABC):
    retry_count = 1
    @abstractmethod
    def send(self, recipient, message) -> None:
        """Business logic on how to send the notification 
        resides with the inidividual notification senders"""
        pass

class SmsSender(NotificationSender):
    retry_count = 2

    def send(self, recipient, message) -> None:
        print("Email Sent")
            

class EmailSender(NotificationSender):
    retry_count = 3
    def send(self, recipient, message) -> None:
        print("Failed to send SMS. Gateway time out")
        raise NotificationSenderError("An error occured")

class PushSender(NotificationSender):
    def send(self, recipient, message) -> None:
        print("Push notification sent")

# --------- Manager classes responsible for instantiating the senders -------

class NotificationManager(ABC):
    def notify(self, recipient, message):
        sender = self.create_sender()
        _retry = 0
        while _retry < sender.retry_count:
            try:   
                sender.send(recipient, message)
                break
            except NotificationSenderError as Err:
                _retry += 1
                print(f"Retrying {_retry} times")
        
        if _retry == sender.retry_count:
            raise RetryFailedError("Failed to send message, try another channel")

    @abstractmethod
    def create_sender(self) -> NotificationSender:
        pass


class SmsNotificationManager(NotificationManager):
    def create_sender(self) -> NotificationSender:
        return SmsSender()


class EmailNotificationManager(NotificationManager):
    def create_sender(self) -> NotificationSender:
        return EmailSender()


class PushNotificationManager(NotificationManager):
    def create_sender(self) -> NotificationSender:
        return PushSender()


def main():
    try:
        sender = EmailNotificationManager()
        sender.notify('', '')
    except RetryFailedError as err:
        sender = SmsNotificationManager()
        sender.notify('', '')

main()