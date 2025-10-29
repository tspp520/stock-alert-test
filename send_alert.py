# send_alert.py (修改版)
import os
import requests
import json
from datetime import datetime
import time

WEBHOOK_URL = os.getenv("WECHAT_WEBHOOK")

if not WEBHOOK_URL:
    raise ValueError("环境变量 WECHAT_WEBHOOK 未设置！")

# 在一分钟内发送 10 条消息，间隔 6 秒
for i in range(10):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # 精确到毫秒
    message = f"[GitHub Actions 测试] 第 {i+1} 条消息 | 执行时间: {current_time}"

    payload = {
        "msgtype": "text",
        "text": {
            "content": message,
        }
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        print(f"✅ 消息 {i+1}/10 发送成功！状态码: {response.status_code}")
    except Exception as e:
        print(f"❌ 消息 {i+1}/10 发送失败: {e}")

    time.sleep(6)  # 每次发送后等待 6 秒，10 条消息共 54 秒，留出 6 秒缓冲
