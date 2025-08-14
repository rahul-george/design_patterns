"""
This file contains a very raw implementation of the notify
"""

from abc import ABC, abstractmethod
import random

class RetryFailedError(Exception):
    pass

class TransientError(Exception):
    pass

class PermanentError(Exception):
    pass

def generate_success(user_choice=None):
    choice = random.randint(0,2) if user_choice is None else user_choice
    if choice == 0:
        return 'success'
    elif choice == 1:
        raise TransientError("Recoverable error")
    else:
        raise PermanentError("Unrecoverable error")


class NotificationSender(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

class EmailSender(NotificationSender):
    retry_count = 2
    def send(self, recipient, message):
        attempt = 0
        while attempt < self.retry_count:
            try:
                generate_success(1)
                print("Email Sent")
                return
            except TransientError as err:
                attempt += 1
                print("Ran into a temporary error")
                print(f"Retrying {attempt}/{self.retry_count} times.. ")
        
        raise RetryFailedError("Exhausted all retry attempts")

class SMSSender(NotificationSender):
    retry_count = 1
    def send(self, recipient, message):
        try:
            generate_success()
            print("SMS Sent")
            return
        except TransientError as err:
            print("Ran into a temporary error")





def main(send_mode='SMS'):
    """
    In this version, the send algorithm is abstracted away by the senders. 
    But initializing the senders are in the main. 

    This is a simple factory. 

    If for each sender, we need a retry mechanism. 
    This is handled within the sender. 

    -- After implementing this for one sender, it is clear that the retry logic is same
    for the next sender also. So probably best to extract that logic out. 

    Any fallback logic is also implemented within the sender. 

    Why do we need to move from Simple Factory to Factory method?

    """
    if send_mode == 'SMS':
        sender: NotificationSender = SMSSender()
    elif send_mode == 'EMAIL':
        sender: NotificationSender = EmailSender()
    else:
        raise AttributeError(f"Not a valid sender mode: {send_mode}")

    try:
        sender.send('', '')
    except PermanentError as err:
        print('Ran into a permanent error')

if __name__ == "__main__":
    main('EMAIL')