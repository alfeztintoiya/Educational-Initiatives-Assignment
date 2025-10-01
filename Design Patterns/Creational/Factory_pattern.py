class Notification:
    def send(self,message):
        pass

class EmailNotification(Notification):
    def send(self,message):
        print(f"Sending Email: {message}")
    
class SMSNotification(Notification):
    def send(self,message):
        print(f"Sending SMS: {message}")

class PushNotification(Notification):
    def send(self,message):
        print(f"Sending Push: {message}")

class NotificationFactory:
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError("Provide Valid Notification Type")

notify = NotificationFactory.create_notification("sms")
notify.send("This is Factory Design Pattern")