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
        print("SMS Sent")
            

class EmailSender(NotificationSender):
    retry_count = 3
    def send(self, recipient, message) -> None:
        print("Failed to send Email. time out")
        raise NotificationSenderError("An error occured")

class PushSender(NotificationSender):
    def send(self, recipient, message) -> None:
        print("Push notification sent")

# --------- Manager classes responsible for instantiating the senders -------

class NotificationManager(ABC):
    def notify(self, recipient, message):
        """The notify method implements the retry logic,
          but the retry count itself is stored in the sender classes"""
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

class FallbackNotifictionManager:
    def __init__(self, managers: list[NotificationManager]) -> None:
        self._managers = managers

    def _notify_with_simple_retry(self, mgr, recipient, message):
        attempt = 0
        sender: NotificationSender = mgr.create_sender()

        while attempt < sender.retry_count:
            try:
                attempt += 1
                sender.send(recipient, message)
                return
            except NotificationSenderError as err:
                # You can also create two classes one for retriable errors 
                # and another for permanent errors
                print(f"Attempt {attempt}/{sender.retry_count}. Retrying...")
        
        # If it comes here, it means it did not return
        raise RetryFailedError("Out of retries")
    
    def notify(self, recipient, message):
        for mgr in self._managers:
            try:
                self._notify_with_retry(mgr, recipient, message)
                return 
            except RetryFailedError as err:
                print(err)
                print("Falling back to next channel")

def main():
    # try:
    #     sender = EmailNotificationManager()
    #     sender.notify('', '')
    # except RetryFailedError as err:
    #     sender = SmsNotificationManager()
    #     sender.notify('', '')

    # With fall back
    sender_manager_with_fallback = FallbackNotifictionManager([
        EmailNotificationManager(),
        SmsNotificationManager()
    ])
    sender_manager_with_fallback.notify('', '')

main()