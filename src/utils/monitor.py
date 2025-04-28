import requests
from utils.telegram import enviar_mensagem_telegram

def consultar_endereco(endereco):
    url_saldo = f"https://blockstream.info/api/address/{endereco}"
    try:
        resposta = requests.get(url_saldo, timeout=50)
        if resposta.status_code == 200:
            dados_saldo = resposta.json()

            funded_txo_sum = dados_saldo.get("chain_stats", {}).get("funded_txo_sum", 0)
            spent_txo_sum = dados_saldo.get("chain_stats", {}).get("spent_txo_sum", 0)
            saldo_satoshis = funded_txo_sum - spent_txo_sum
            saldo_btc = saldo_satoshis / 100_000_000
            total_transacoes = dados_saldo.get("chain_stats", {}).get("tx_count", 0)
            mensagem = f"🏦 Endereço: {endereco}\n💰 Saldo atualizado: {saldo_btc:.8f} BTC ({saldo_satoshis} satoshis)\n🔄 Total de transações: {total_transacoes}"
            enviar_mensagem_telegram(mensagem)
        else:
            print(f"Erro ao acessar saldo para o endereço {endereco}: {resposta.json()}")
    except requests.exceptions.Timeout:
        print(f"Erro: Tempo limite excedido ao consultar o endereço {endereco}.")
    except requests.exceptions.ConnectionError as e:
        print(f"Erro de conexão ao consultar o endereço {endereco}: {str(e)}")
    except Exception as e:
        print(f"Erro ao consultar o endereço {endereco}: {str(e)}")
