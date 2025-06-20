#!/usr/bin/env python3
import os
import requests
import time
from datetime import datetime

BOT_TOKEN = "7151382731:AAGb1r6ACJE-xkMxFiW4Ml3wD1X5rKOPTkc"

print('π Twin Gate Bot εεδΈ­...')

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
    try:
        response = requests.post(url, json=data, timeout=10)
        return response.json()
    except Exception as e:
        print(f'β ηΌθ¨θͺ€θͺ€: {e}')
        return None

def handle_start(chat_id, first_name):
    """θη /start ε½δ»€"""
    message = f"""π <b>Hello {first_name}!</b> Welcome to Twin Gate!

π <b>Twin3.ai Human Identity Verification System</b>

Prove your humanity and earn your digital identity through our advanced three-stage verification process.

π― <b>Your Current Status:</b>
β’ Verification Level: 0/3
β’ SBT Tokens: 0
β’ Reputation Score: 0

ο <b>Available Commands:0/b>
β’ /start - Show this welcome message
β’ /verify - Begin verification process
β’ /help - Show help information
β’ /status - Check your verification status

ο <b>Get Started:</b>
Click /verify to begin your human identity verification journey!"""
    send_message(chat_id, message)

def handle_verify():
    """θη /verify ε½δ»€"""
    return """π <b>Verification System</b>

Welcome to the Twin3.ai Human Identity Verification System!

π€ <b>Three-Stage Verification Process:</b>

<b>Stage 1</b> - Basic Verification: Google reCAPTCHA
π€ <b>Stage 2</b> - Phone Verification: SMS Verification
<b>Stage 3</b> - Biometric Verification: Twin3.ai API

π° <b>Progress Rewards:</b>
β’ Must complete each stage in order
>β’ Earn SBT tokens upon completion
β’ Minimum passing score: 100 points

π <b>Ready to Start?</b>
The verification system is currently under development. Please check back soon!"""

def main():
    print('π€%Twin Gate Bot ε·²εε')
    
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
                        
                        print(f'π€ {first_name} ({chat_id}): {text}')
                        
                        if text == '/start':
                            handle_start(chat_id, first_name)
                        elif text == '/verify':
                            send_message(chat_id, handle_verify())
                        elif text == '/help':
                            help_msg = """π <b>Help Information</b>

ο <b>Available Commands:0/b>
β’ /start - Show welcome message
β’ /verify - Begin verification process
β’ /help - Show this help message
β’ /status - Check your verification status

π <b>Contact Information:</b>
β’ Telegram Bot: @twin3bot
β’ Website: twin3.ai
β’ Support: contact@twin3.ai

π <b>Need Help?</b>
If you encounter any issues, please contact our support team."""
                            send_message(chat_id, help_msg)
                        elif text == '/status':
                            status_msg = f"""π <b>Your Verification Status:0/b>

Hello {first_name}!

ο <b>Current Progress:</b>
β’ Verification Level: 0/3
β’ SBT Tokens: 0
β’ Reputation Score: 0

π€ <b>Next Steps:0/b>
1. Click /verify to start your verification journey
2. Complete Stage 1: Basic Verification
3. Proceed to Stage 2: Phone Verification
4. Finish with Stage 3: Biometric Verification

π Ready to begin? Use /verify!"""
                            send_message(chat_id, status_msg)
                        else:
                            default_msg = f"""Hello {first_name}! I'm the Twin Gate Bot.

I didn't understand that command. Here are the available commands:

β’ /start - Show welcome message
β’ /verify - Begin verification process
β’ /help - Show help information
β’ /status - Check your verification status

Please try one of these commands!"""
                            send_message(chat_id, default_msg)
            else:
                print(f'β η²εζ΄ζ°ε€±ζ: {updates}')
            
        except KeyboardInterrupt:
            print('\nβ Bot ε·²εζ­’')
            break
        except Exception as e:
            print(f'β ιθ‘ι―θͺ€: {e}')
            time.sleep(5)
        
        time.sleep(1)

if __name__ == '__main__':
    main()
