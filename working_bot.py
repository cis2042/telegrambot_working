#!/usr/bin/env python3
import requests
import time
import json
from datetime import datetime

BOT_TOKEN = "7151382731:AAGb1r6ACJG-xkMxFiW4Ml3wD1X5rKOPTkc"
ADMIN_CHAT_ID = "589541800"

def send_message(chat_id, text, parse_mode='HTML'):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode}
    try:
        response = requests.post(url, json=data, timeout=10)
        return response.json()
    except Exception as e:
        print(f'❌ 發訁錯詤: {e}')
        return None

def get_updates(offset=0):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
    params = {'offset': offset, 'timeout': 30}
    try:
        response = requests.get(url, params=params, timeout=35)
        return response.json()
    except Exception as e:
        print(f'❌ 獲取更新錯詤: {e}')
        return {'ok': False, 'error': str(e)}

def handle_message(message):
    chat_id = str(message['chat']['id'])
    text = message.get('text', '')
    user_name = message['from'].get('first_name', '用戶')
    
    print(f'👤 {user_name} ({chat_id}): {text}')
    
    if text == '/start':
        welcome_msg = f"""🚀 <b>Twin Gate Bot 歠迎 {user_name}!</b>

🤖 <b>Twin Gate Telegram Bot</b>
<i>人類身份驗證服動</i>

� <b>GCP 部署狀慁:</b>
- 🌐 VM IP: 35.185.141.238
- 🗄️ 資料庫 IP: 35.194.208.240
- 🤖 <b>Bot:</b> [@twin3bot](https://t.me/twin3bot) - 正常運行
- 💰 <b>頔4估費品:</b> 約 $35/月

📱 <b>支援的命令:</b>
- <code>/start</code> - 啟動 Bot 並显示歠迎
- <code>/verify</code> - 進入三階段��證系統
- <code>/help</code> - 顯示幫助信息

� <b>快速開始</b>
進過上面的按邕進行部署!”""
        send_message(chat_id, welcome_msg)
        
    elif text == '/verify':
        verify_msg = f"""🚀 <b>驗證系統</b>

🚀 <b>三階嫭i��證系統:</b>

🤖 <b>Stage 1</b> - 基本禦_��#��iGoogle rECAPTCHA
🤖 <b>Stage 2</b> - 手機驗證：SMS 驗證
🤖 <b>Stage 3</b> - 生物識別驗證：Twin3.ai API

💰 <b>進過進度:</b>
- 必須按肺完成各級驗證
- 完成後可獲得 SBT (鑄造在网上身份詉明)
- 通過門檻: ≥100 分

� <b>快速開始</b>
目前正在開發中，請使用下面連結進行驗證！"""
        send_message(chat_id, verify_msg)
        
    elif text == '/help':
        help_msg = f"""𓒞 <b>Twin Gate Bot 幫助信息</b>

🚀 <b>主♁功能></b>
- 🤖 人類身份驗證系統
- 📱GCP 雿端部署和運行
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
        send_message(chat_id, help_msg)
        
    else:
        default_msg = f"""🤖 <b>感谜！{user_name}</b>

🚀 我是 Twin Gate Bot 。请使用以下命令：

- 🚀 <code>/start</code> - 查看 Bot 功能
- <code>/verify</code> - 進入禦_��#��ig��統
- 🚀 <code>/help</code> - 查看幫助信息

💰 <b>現在部署版本:</b>
- VM IP: 35.185.141.238
- 資料庫 IP: 35.194.208.240
- 頔4估費品: ~$35/月"""
        send_message(chat_id, default_msg)

def main():
    print('🤖%Twin Gate Bot 已啟動')
    send_message(ADMIN_CHAT_ID, f"""✅ <b>Twin Gate Bot GCP 部署成功!</b>

🤖 <b>版本:</b> 1.0.3-gcp
⏰ <b>啟動時間:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
💰 <b>平台:</b> Google Cloud Platform
💰 <b>Vm IP:</b> 35.185.141.238
🗄️ <b>DB IP:</b> 35.194.208.240

🤖 <b>Bot 现在在 GCP 上運行！</b>
快測試 @twin3bot 的功能。""")
    
    last_update_id = 0
    
    while True:
        try:
            updates = get_updates(last_update_id)
            
            if updates.get('ok') and updates['result']:
                for update in updates['result']:
                    last_update_id = update['update_id'] + 1
                    
                    if 'message' in update:
                        handle_message(update['message'])
            else:
                print(f'“ 玲取更新失敗: {updates}')
            
        except KeyboardInterrupt:
            print('\n✀ Bot 已停止')
            break
        except Exception as e:
            print(f'❌ 運行錯誤: {e}')
            time.sleep(5)
        
        time.sleep(1)

if __name__ == '__main__':
    main()
