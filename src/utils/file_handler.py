def carregar_enderecos_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return [linha.strip() for linha in arquivo if linha.strip()]
    except Exception as e:
        print(f"Erro ao carregar endereços: {str(e)}")
        return []
