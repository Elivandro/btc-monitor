import requests
import os

def enviar_mensagem_telegram(mensagem):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensagem
    }
    try:
        resposta = requests.post(url, json=payload)
        if resposta.status_code == 200:
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Erro ao enviar mensagem: {resposta.json()}")
    except Exception as e:
        print(f"Erro ao conectar ao Telegram: {str(e)}")
