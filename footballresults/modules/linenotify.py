import requests
from app_admins.models import AdminSetting

def send_line_notification(message):
    setting = AdminSetting.objects.first()
    token = setting.line_api
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    payload = {
        'message': message,
    }
    response = requests.post(url, headers=headers, data=payload)
    return response

if __name__ == '__main__':
    # Replace with your Line Notify token
    line_token = 'YOUR_LINE_NOTIFY_TOKEN'
    
    notification_message = 'Hello from Python!'
    response = send_line_notification(notification_message, line_token)

    if response.status_code == 200:
        print('Notification sent successfully')
    else:
        print('Notification failed')
