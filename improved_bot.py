#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Twin Gate Telegram Bot - Improved Version
Version: 1.0.2-improved
Status: 改向版本
\"""

import os
import requests
import time
import json
from datetime import datetime
from typing import Dict, Any

# 配置
BOT_TOKEN = '7151382731:AAGb1r6ACJG-x�MxFiW4Ml3wD1X5rKOPTkc'
ADMIN_CHAT_ID = '589541800'

# GCP 部署狀慁
GCP_VM_IP = '35.185.141.238'
GCP_DB_IP = '35.194.208.240'

print('🚀 Twin Gate Bot 啟動中...')
print(f'GCP 部署狀慁: VM {GCP_VM_IP}, DB {GCP_DB_IP}')
