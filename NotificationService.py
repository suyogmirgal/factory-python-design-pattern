from NotificationFactory import NotificationFactory
from NotificationDetail import NotificationDetail

types = ['EMAIL', 'SMS', 'PUSH']

for type in types:
    notification = NotificationFactory().create_notification(type=type)
    notification.notify_user(NotificationDetail(user='Suyog', message='Hello!'))
