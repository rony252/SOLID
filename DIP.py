#DIP
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_notification(self) -> None:
        pass

class SMSNotification(Notification):
    def send_notification(self) -> None:
        print("Sending SMS notification")


class EmailNotification(Notification):
    def send_notification(self) -> None:
        print("Sending Email notification")


class NotificationService:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self) -> None:
        self.notification.send_notification()


sms = SMSNotification()
email = EmailNotification()

 
sms_service = NotificationService(sms)
sms_service.send()  

email_service = NotificationService(email)
email_service.send()  

