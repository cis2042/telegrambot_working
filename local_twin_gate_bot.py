#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Twin Gate Telegram Bot - GCP 部署版本
Version: 1.0.3-gcp
Status: 生産就改

Features:
- 🤖 多効言支捴 (繁體中文、觀語、德誟)
- 🚀 GCP 自倕化部署
- 📱 PostgreSQL 資料庫支援
- 🌐 全天候運行
"""

import os
import requests
import time
import json
from datetime import datetime
from typing import Dict, Any

# 配置
BOT_TOKEN = '7151382731:AAGb1r6ACJG-xkMxFiW4Ml3wD1X5rKOPTkc'
ADMIN_CHAT_ID = '589541800'

# GCP 部署狀慁
GCP_VM_IP = '35.185.141.238'
GCP_DB_IP = '35.194.208.240'

print('🚀 Twin Gate Bot 啟動中...')
print(f'GCP 部署狀慁: VM {GCP_VM_IP}, DB {GCP_DB_IP}')

def send_message(chat_id: str, text: str, parse_mode: str = 'HTML') -> Dict[str, Any]:
    """傰送文字消息到指定 chat """
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': parse_mode
    }
    
    try:
        response = requests.post(url, json=data, timeout=10)
        result = response.json()
        if result.get('ok'):
            print(f'★ 成功傳送: {chat_id}')
        else:
            print(f'❌ 傰送失敗: {result}')
        return result
    except Exception as e:
        print(f'❌ 傰送錯詤: {e}')
        return {'ok': False, 'error': str(e)}

def get_updates(offset: int = 0) -> Dict[str, Any]:
    """獲取新的消息更新"""
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
    params = {'offset': offset, 'timeout': 30}
    
    try:
        response = requests.get(url, params=params, timeout=35)
        return response.json()
    except Exception as e:
        print(f'“ 药取更新誤誤: {e}')
        return {'ok': False, 'error': str(e)}

def handle_message(message: Dict[str, Any]) -> None:
    """蕕、閜文字消息"""
    chat_id = str(message['chat']['id'])
    text = message.get('text', '')
    user_name = message['from'].get('first_name', '用戶')
    
    print(f'👤 {user_name} ({chat_id}): {text}')
    
    if text == '/start':
        welcome_message = f"""🚀 <b>Twin Gate Bot 歡迎 {user_name}!</b>

🤖 <b>Twin Gate Telegram Bot</b>
<i>人類身份驗證系統服動</i>

🌐 <b>GCP 部署狀慁:</b>
- 🌐 VM IP: <code>{GCP_VM_IP}</code>
- 🗄️ 資料庫 IP: <code>{GCP_DB_IP}</code>
- 🤖 <b>Bot:</b> [@twin3bot](https://t.me/twin3bot) - 正常運行
- 💰 <b>頔4估費品:</b> 約 $35/月

📱 <b>支援的命令:</b>
- <code>/start</code> - 啟動 Bot 並显示歠迎
- <code>/verify</code> - 進入三階段��證系統
- <code>/help</code> - 顯示幫助信息

� <b>快速開始</b>
進過上面的按邕進行部署！"""
        send_message(chat_id, welcome_message)
        
    elif text == '/verify':
        verify_message = f"""🚀 <b>驗證系統</b>

� <b>三階段��證系統系統:</b>

🤖 <b>Stage 1</b> - 基示驗證：Google rECAPTCHA
🤖 <b>Stage 2</b> - 手機驗證：SMS 驗證
🤖 <b>Stage 3</b> - 生物識別驗證：Twin3.ai API

💰 <b>進過進度:</b>
- 必須按肺完成各級驗證
- 完成後可獲得 SBT (鑄造在网上身份詉明)
- 通過門檻: ≥100 分

� <b>快速開始</b>
目前正在開發中，請使用下面連結進行驗證！"""
        send_message(chat_id, verify_message)
        
    elif text == '/help':
        help_message = f"""💞 <b>Twin Gate Bot 帯助信息</b>

� <b>主要功能:</b>
- 🤖 人類身份驗證系統
- 📱 GCP 雿端部署和運行
- 🗄️ PostgreSQL 資料庫管理
- 🌐 全天候運行

📱 <b>支援的命令:</b>
- <code>/start</code> - 啟動 Bot 並显示歠迎
- <code>/verify</code> - 進入三階段��證系統
- <code>/help</code> - 顯示幫助信息

� <b>聯繫方式:</b>
- <b>Telegram Bot</b>: [@twin3bot](https://t.me/twin3bot)
- <b>GitHub</b>: [https://github.com/cis2042/telegrambot](https://github.com/cis2042/telegrambot)

� <b>如有閏顏:</b>
请聯繫管理員或在 GitHub 上提出問題。"""
        send_message(chat_id, help_message)
        
    else:
        # 其他的指令或不公識的指令
        default_message = f"""🤖 <b>思訝！ {user_name}</b>

� 我是 Twin Gate Bot 。请使用以下命令：

- 🚀 <code>/start</code> - 查看 Bot 功能
- 🚀 <code>/verify</code> - 進入驗證系統
- 🚀 <code>/help</code> - 查看幫助信息

💰 <b>現在部署版本:</b>
- VM IP: <code>{GCP_VM_IP}</code>
- 資料庫 IP: <code>{GCP_DB_IP}</code>
- 預訌資用: ~$35/月"""
        send_message(chat_id, default_message)

def main():
    """主程式豄入"""
    print('🤖 Twin Gate Bot 已夕動')
    
    # 傰送啟動成功通知
    send_message(ADMIN_CHAT_ID, f"""★ <b>Twin Gate Bot GCP 部署成功!</b>

🤖 <b>版本:</b> 1.0.3-gcp
⏰ <b>啟動時間:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
💰 <b>平台:</b> Google Cloud Platform
💰 <b>Vm IP:</b> {GCP_VM_IP}
�️ <b>DB IP:</b> {GCP_DB_IP}

🤖 <b>Bot 現在在 GCP 上運行！</b>
快測試 @twin3bot 的功能。""")
    
    last_update_id = 0
    
    while True:
        try:
            # 獲取新消息
            updates = get_updates(last_update_id)
            
            if updates.get('ok') and updates['result']:
                for update in updates['result']:
                    last_update_id = update['update_id'] + 1
                    
                    if 'message' in update:
                        handle_message(update['message'])
            else:
                print(f'❌ 獲取新消息失敗: {updates}')
            
        except KeyboardInterrupt:
            print('\n🚀 Bot 已停止')
            break
        except Exception as e:
            print(f'“ 運行誤誤: {e}')
            time.sleep(5)
        
        # 等待 5 秒再樢查
        time.sleep(1)

if __name__ == '__main__':
    main()
