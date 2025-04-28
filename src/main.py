import time
import os
from dotenv import load_dotenv
from utils.file_handler import carregar_enderecos_do_arquivo
from utils.monitor import consultar_endereco

def monitorar_varios_enderecos(enderecos):
    for endereco in enderecos:
        consultar_endereco(endereco)

def main():
    load_dotenv()
    arquivo_enderecos = os.getenv("ADDRESSES_FILE")
    enderecos_bitcoin = carregar_enderecos_do_arquivo(arquivo_enderecos)

    if not enderecos_bitcoin:
        print("Nenhum endereço encontrado para monitorar.")
        return

    try:
        while True:
            print("Iniciando verificação de endereços...")
            monitorar_varios_enderecos(enderecos_bitcoin)
            print("Verificação concluída. Aguardando para próxima execução...")
            time.sleep(300) 
    except KeyboardInterrupt:
        print("\nMonitoramento interrompido pelo usuário. Encerrando o programa com segurança.")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
    finally:
        print("Aplicação finalizada.")

if __name__ == "__main__":
    main()
