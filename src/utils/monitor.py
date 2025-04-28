import requests
from utils.telegram import enviar_mensagem_telegram

estado_anterior = {}

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
            estado_anterior_do_endereco = estado_anterior.get(endereco, {"saldo": None, "total_transacoes": None})

            if saldo_satoshis != estado_anterior_do_endereco["saldo"] or total_transacoes != estado_anterior_do_endereco["total_transacoes"]:
                mensagem = f"🏦 Endereço: {endereco}\n💰 Saldo atualizado: {saldo_btc:.8f} BTC ({saldo_satoshis} satoshis)\n🔄 Total de transações: {total_transacoes}"
                enviar_mensagem_telegram(mensagem)
                estado_anterior[endereco] = {"saldo": saldo_satoshis, "total_transacoes": total_transacoes}
            else:
                print(f"Nenhuma alteração detectada para o endereço: {endereco}")
        else:
            print(f"Erro ao acessar saldo para o endereço {endereco}: {resposta.json()}")
    except requests.exceptions.Timeout:
        print(f"Erro: Tempo limite excedido ao consultar o endereço {endereco}.")
    except requests.exceptions.ConnectionError as e:
        print(f"Erro de conexão ao consultar o endereço {endereco}: {str(e)}")
    except Exception as e:
        print(f"Erro ao consultar o endereço {endereco}: {str(e)}")
