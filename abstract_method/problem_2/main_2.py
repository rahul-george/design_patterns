"""
Goal: 
1. Implement a notification system. 
2. The notification system uses email as the notification channel. 
3. If certain type of errors occur, the system should retry.
4. Add new notification channel - SMS 
5. SMS notification channel also should have a retry. 
6. retry is channel specific. 
7. Refactor simple factory to factory method. 
"""
from abc import ABC, abstractmethod
import random


class RetryFailedError(Exception):
    pass

class TransientError(Exception):
    pass

class PermanentError(Exception):
    pass

def generate_response(user_choice=None):
    choice = random.randint(0,2) if user_choice is None else user_choice
    if choice == 0:
        return 'success'
    elif choice == 1:
        raise TransientError("Recoverable error")
    else:
        raise PermanentError("Unrecoverable error")


class NotificationSender(ABC):
    max_retry_count = 0
    @abstractmethod
    def send(self, recipient, message):
        pass


class EmailSender(NotificationSender):
    max_retry_count = 2
    def __init__(self, server, api_key) -> None:
        pass

    def send(self, recipient: str, message: str) -> None:
        generate_response(1)
        print("Email Sent")
    

class SmsSender(NotificationSender):
    max_retry_count = 2
    def __init__(self, gateway, api_key) -> None:
        pass

    def send(self, recipient: str, message: str) -> None:
        generate_response(0)
        print("SMS Sent")
    

class NotificationManager(ABC):
    @abstractmethod
    def create_sender(self) -> NotificationSender:
        """Override the create sender in the specific manager classes to create it's instance. 
        Converted from simple factory to factory method. 
        Benefit: 
        1. When new channels are added, the simple factory conditional need not change. 
        2. Different creation workflows per product family. 
        3. Client need not worry about the creation of Senders.         
        """
        pass

    def notify(self, recipient: str, message: str):
        sender = self.create_sender()

        attempt = 0
        while attempt < sender.max_retry_count:
            try:
                generate_response(0)
                sender.send(recipient, message)
                return
            except TransientError as err:
                attempt += 1
                print("Ran into a temporary error")
                print(f"Retrying {attempt}/{sender.max_retry_count} times.. ")
        
        raise RetryFailedError("Exhausted all retry attempts")
    

class EmailNotificationMgr(NotificationManager):
    def create_sender(self) -> NotificationSender:
        mail_server = ''
        api_key = ''
        return EmailSender(mail_server, api_key)
    

class SmsNotificationMgr(NotificationManager):
    def create_sender(self) -> NotificationSender:
        sms_gateway = ''
        api_key = ''
        return SmsSender(sms_gateway, api_key)

class FallbackNotificationMgr:
    def __init__(self, managers: list[NotificationManager]) -> None:
        self._managers = managers
    
    def notify(self, recipient: str, message: str):

        for mgr in self._managers:
            sender = mgr.create_sender()
            print(f"Attempting to send via {sender.__class__.__name__}")

            attempt = 0
            while attempt < sender.max_retry_count:
                try:
                    sender.send(recipient, message)
                    return
                except TransientError as err:
                    attempt += 1
                    print("Ran into a temporary error")
                    print(f"Retrying {attempt}/{sender.max_retry_count} times.. ")
            
            print("Exhausted all retry attempts")
        raise PermanentError("All notification channels failed.")
        

def notify(recipient, message):
    """Use the notify function directly in other places"""
    notification_mgr = FallbackNotificationMgr([EmailNotificationMgr(), 
                                                SmsNotificationMgr()])
    notification_mgr.notify(recipient, message)


def main():
    notify('', '')


if __name__ == "__main__":
    main()