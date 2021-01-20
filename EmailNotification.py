from Notification import Notification
from NotificationDetail import NotificationDetail


class EmailNotification(Notification):

    def __init__(self, host, user_name, password):
        self.host = host
        self.user_name = user_name
        self.password = password

    def notify_user(self, notification_detail):
        print("sending email notification")