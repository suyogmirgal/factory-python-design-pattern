from Notification import Notification
from NotificationDetail import NotificationDetail


class SMSNotification(Notification):

    def __init__(self, user_name, auth_key):
        self.user_name = user_name
        self.auth_key = auth_key

    def notify_user(self, notification_detail):
        print("sending SMS notification")