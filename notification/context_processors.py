from notification.models import Notification

def notifications(request):
    if request.user.is_authenticated:
        return {"notificactions": request.user.notifications.filter(is_read= False)}
    else:
        return{"notifications":[]}
    