#!/usr/bin/env python3
import os
import requests
import time
from datetime import datetime

BOT_TOKEN = "7151382731:AAGb1r6ACJE-xkMxFiW4Ml3wD1X5rKOPTkc"

print('🚀 Twin Gate Bot 啟動中...')

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
    try:
        response = requests.post(url, json=data, timeout=10)
        return response.json()
    except Exception as e:
        print(f'“ 發訁誤誤: {e}')
        return None

def handle_start(chat_id, first_name):
    """處理 /start 命令"""
    message = f"""👋 <b>Hello {first_name}!</b> Welcome to Twin Gate!

🌍 <b>Twin3.ai Human Identity Verification System</b>

Prove your humanity and earn your digital identity through our advanced three-stage verification process.

🎯 <b>Your Current Status:</b>
• Verification Level: 0/3
• SBT Tokens: 0
• Reputation Score: 0

� <b>Available Commands:0/b>
• /start - Show this welcome message
• /verify - Begin verification process
• /help - Show help information
• /status - Check your verification status

� <b>Get Started:</b>
Click /verify to begin your human identity verification journey!"""
    send_message(chat_id, message)

def handle_verify():
    """處理 /verify 命令"""
    return """🚀 <b>Verification System</b>

Welcome to the Twin3.ai Human Identity Verification System!

🤖 <b>Three-Stage Verification Process:</b>

<b>Stage 1</b> - Basic Verification: Google reCAPTCHA
🤖 <b>Stage 2</b> - Phone Verification: SMS Verification
<b>Stage 3</b> - Biometric Verification: Twin3.ai API

💰 <b>Progress Rewards:</b>
• Must complete each stage in order
>• Earn SBT tokens upon completion
• Minimum passing score: 100 points

🚀 <b>Ready to Start?</b>
The verification system is currently under development. Please check back soon!"""

def main():
    print('🤖%Twin Gate Bot 已啟動')
    
    last_update_id = 0
    
    while True:
        try:
            url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
            params = {'offset': last_update_id, 'timeout': 30}
            
            response = requests.get(url, params=params, timeout=35)
            updates = response.json()
            
            if updates.get('ok') and updates['result']:
                for update in updates['result']:
                    last_update_id = update['update_id'] + 1
                    
                    if 'message' in update:
                        message = update['message']
                        chat_id = message['chat']['id']
                        text = message.get('text', '')
                        first_name = message['from'].get('first_name', 'User')
                        
                        print(f'👤 {first_name} ({chat_id}): {text}')
                        
                        if text == '/start':
                            handle_start(chat_id, first_name)
                        elif text == '/verify':
                            send_message(chat_id, handle_verify())
                        elif text == '/help':
                            help_msg = """𓒞 <b>Help Information</b>

� <b>Available Commands:0/b>
• /start - Show welcome message
• /verify - Begin verification process
• /help - Show this help message
• /status - Check your verification status

📘 <b>Contact Information:</b>
• Telegram Bot: @twin3bot
• Website: twin3.ai
• Support: contact@twin3.ai

🚀 <b>Need Help?</b>
If you encounter any issues, please contact our support team."""
                            send_message(chat_id, help_msg)
                        elif text == '/status':
                            status_msg = f"""📊 <b>Your Verification Status:0/b>

Hello {first_name}!

� <b>Current Progress:</b>
• Verification Level: 0/3
• SBT Tokens: 0
• Reputation Score: 0

🤖 <b>Next Steps:0/b>
1. Click /verify to start your verification journey
2. Complete Stage 1: Basic Verification
3. Proceed to Stage 2: Phone Verification
4. Finish with Stage 3: Biometric Verification

🚀 Ready to begin? Use /verify!"""
                            send_message(chat_id, status_msg)
                        else:
                            default_msg = f"""Hello {first_name}! I'm the Twin Gate Bot.

I didn't understand that command. Here are the available commands:

• /start - Show welcome message
• /verify - Begin verification process
• /help - Show help information
• /status - Check your verification status

Please try one of these commands!"""
                            send_message(chat_id, default_msg)
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
