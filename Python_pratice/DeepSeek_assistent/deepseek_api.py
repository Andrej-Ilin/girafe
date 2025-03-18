import requests
from config import DEEPSEEK_API_URL

def ask_deepseek(prompt):
    payload = {
        "model": "deepseek-r1",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(DEEPSEEK_API_URL, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    return "Ошибка получения ответа от DeepSeek-R1."