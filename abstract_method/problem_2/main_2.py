"""
Goal: 
1. Implement a notification system. 
2. The notification system uses email as the notification channel. 
3. If certain type of errors occur, the system should retry.
4. Add new notification channel - SMS 
5. SMS notification channel also should have a retry. 
6. retry is channel specific. 
"""
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


class EmailSender():
    max_retry_count = 2
    def __init__(self) -> None:
        pass

    def send(self, recipient: str, message: str) -> None:
        attempt = 0
        while attempt < self.max_retry_count:
            try:
                generate_response(1)
                print("Email Sent")
                return
            except TransientError as err:
                attempt += 1
                print("Ran into a temporary error")
                print(f"Retrying {attempt}/{self.max_retry_count} times.. ")
        
        raise RetryFailedError("Exhausted all retry attempts")
    

class SmsSender():
    max_retry_count = 2
    def __init__(self) -> None:
        pass

    def send(self, recipient: str, message: str) -> None:
        attempt = 0
        while attempt < self.max_retry_count:
            try:
                generate_response(1)
                print("SMS Sent")
                return
            except TransientError as err:
                attempt += 1
                print("Ran into a temporary error")
                print(f"Retrying {attempt}/{self.max_retry_count} times.. ")
        
        raise RetryFailedError("Exhausted all retry attempts")
        

def notify(recipient, message):
    """Use the notify function directly in other places"""
    sender = SmsSender()
    sender.send(recipient, message)


def main():
    notify('', '')


if __name__ == "__main__":
    main()