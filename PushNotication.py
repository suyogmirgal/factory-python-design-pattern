from Notification import Notification
from NotificationDetail import NotificationDetail


class PushNotification(Notification):

    def __init__(self):
        pass

    def notify_user(self, notification_detail):
        print("sending Push notification")