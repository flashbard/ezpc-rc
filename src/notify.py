from notifypy import Notify

def create_notification(title, message=None, icon=None):
    notification = Notify()

    notification.application_name = "ezpc-rc"
    notification.title = title

    if message:
        notification.message = message
    
    if icon:
        notification.icon = icon

    notification.send(block=False)
