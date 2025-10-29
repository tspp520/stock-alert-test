# send_alert.py
import os
import requests
import json
from datetime import datetime

# 从环境变量读取 Webhook URL
WEBHOOK_URL = os.getenv("WECHAT_WEBHOOK")

if not WEBHOOK_URL:
    raise ValueError("环境变量 WECHAT_WEBHOOK 未设置！请检查 GitHub Actions Secrets 配置。")

# 生成一条包含当前时间戳的消息，确保每次内容不同
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = f"[GitHub Actions 测试] 本次执行时间: {current_time}。这是第 {int(datetime.now().timestamp()) % 1000} 条消息。"

# 构造请求数据
payload = {
    "msgtype": "text",
    "text": {
        "content": message,
        # 可选：@所有人
        # "mentioned_list": ["@all"]
    }
}

# 发送 POST 请求
try:
    response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
    print(f"✅ 消息发送成功！状态码: {response.status_code}")
    print(f"📌 消息内容: {message}")
except Exception as e:
    print(f"❌ 消息发送失败: {e}")
