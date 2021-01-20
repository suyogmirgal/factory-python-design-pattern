from EmailNotification import EmailNotification
from SMSNotification import SMSNotification
from PushNotication import PushNotification


class NotificationFactory:

    def create_notification(self, type):

        if type == 'EMAIL':
            return EmailNotification(host='gmail.com', user_name='suyogm', password='suyog@123')
        elif type == 'SMS':
            return SMSNotification(user_name='suyogm', auth_key='123-xyz')
        elif type == 'PUSH':
            return PushNotification()
