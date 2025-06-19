from apprise import NotifyType
from apprise.decorators import notify

import json
import requests

@notify(on="onebot://user:token@backend:port")
def my_wrapper(body, meta, title='', notify_type=NotifyType.INFO, *args, **kwargs):
    url = meta.host + ':' + meta.port
    user_id = meta.user
    token = meta.token

    payload = json.dumps({
        'user_id': user_id,
        'message': [
            {
                'type': 'text',
                'data': {
                    'text': body
                }
            }
        ]
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code != 200:
        return False
    else:
        return True
