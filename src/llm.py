# src/llm.py

import os
import openai

class LLM:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key

    def generate_daily_report(self, markdown_content):
        prompt = f"Please summarize the following project updates into a formal daily report:\n\n{markdown_content}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
