"""
Goal: 
1. Implement a notification system. 
2. The notification system uses email as the notification channel. 
3. If certain type of errors occur, the system should retry.
4. Add new notification channel - SMS 
5. SMS notification channel also should have a retry. 
6. retry is channel specific. 
"""
from abc import ABC, abstractmethod
import random
import smtplib


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
        print("Email Sent")
    

class SmsSender(NotificationSender):
    max_retry_count = 2
    def __init__(self, gateway, api_key) -> None:
        pass

    def send(self, recipient: str, message: str) -> None:
        print("SMS Sent")
    

class NotificationManager:
    def __init__(self) -> None:
        pass

    def create_sender(self, mode: str) -> NotificationSender:
        """Delegated the creation of sender object based on the mode parameter to this simple factory"""
        if mode == 'SMS':
            sms_gateway = ''
            api_key = ''
            return SmsSender(sms_gateway, api_key)
        elif mode == 'EMAIL':
            mail_server = ''
            api_key = ''
            return EmailSender(mail_server, api_key)
        else: 
            raise NotImplementedError(f"{mode} notification channel is not implemented")

    def notify(self, mode: str, recipient: str, message: str):
        sender = self.create_sender(mode)

        attempt = 0
        while attempt < sender.max_retry_count:
            try:
                generate_response(1)
                sender.send(recipient, message)
                return
            except TransientError as err:
                attempt += 1
                print("Ran into a temporary error")
                print(f"Retrying {attempt}/{sender.max_retry_count} times.. ")
        
        raise RetryFailedError("Exhausted all retry attempts")
        

def notify(recipient, message):
    """Use the notify function directly in other places"""
    notification_mgr = NotificationManager()
    notification_mgr.notify('EMAIL', recipient, message)


def main():
    notify('', '')


if __name__ == "__main__":
    main()