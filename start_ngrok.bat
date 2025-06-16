@echo off
cd C:\Users\Lenovo\tradingview_bot
call venv\Scripts\activate.bat
start cmd /k "ngrok http 8000"
