# Aplicação feita com python para monitorar movimentações em endeços de bitcoin

renomeie o .env.example para .env usando `cd src/ && cp .env.example .env`

consiga o `TELEGRAM_BOT_TOKEN` no telegram: [Botfather](https://telegram.me/BotFather),
consiga o `TELEGRAM_CHAT_ID` no `https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates`

certifique-se de criar o arquivo `src/addresses.txt`com a lista de endereços que deseja monitorar.

## Rodando o código
`cd src/ && python -B main.py`

## Rodando o python de um container docker

### Monte a image
`docker compose build --no-cache`

### Execute a imagem
`docker compose run --rm btc-finder`