# src/config.py

import os

class Config:
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.update_interval = int(os.getenv('UPDATE_INTERVAL', '86400'))  # 默认每天更新
        self.subscriptions_file = os.getenv('SUBSCRIPTIONS_FILE', 'subscriptions.json')
        self.notification_settings = {
            'email': os.getenv('NOTIFICATION_EMAIL'),
            'slack_webhook': os.getenv('SLACK_WEBHOOK')
        }
