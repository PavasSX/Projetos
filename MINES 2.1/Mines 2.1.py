import random
import time
import telegram
import asyncio

# Substitua 'YOUR_BOT_TOKEN' pelo token que você recebeu do BotFather
bot_token = '6686159547:AAFyzn9cmTy3gt75V9kM9r-z_7jMGlGvU5U'

# Crie uma instância do bot
bot = telegram.Bot(token=bot_token)

# Substitua 'YOUR_CHANNEL_ID' pelo ID do seu grupo (começa com @)
group_id = '-901291737'

async def enviar_quadrado_e_mensagem(tamanho, num_uns):
    if num_uns > tamanho ** 2:
        raise ValueError(f"Erro: O número de bombas ({num_uns}) excede o tamanho do quadrado ({tamanho}x{tamanho}). O número máximo de bombas permitido é {tamanho ** 2}.")

    quadrado = [['💣' for _ in range(tamanho)] for _ in range(tamanho)]

    posicoes = [(i, j) for i in range(tamanho) for j in range(tamanho)]
    random.shuffle(posicoes)

    for i in range(num_uns):
        linha, coluna = posicoes[i]
        quadrado[linha][coluna] = '💎'

    # Criar uma representação em texto do quadrado
    texto_quadrado = '\n'.join([' '.join(map(str, linha)) for linha in quadrado])

    # Criar a mensagem de texto com todas as informações
    mensagem = f"KKKKK É O PAVÃO CARALHOO\n\nDuas Tentativas nessa porra, sem choro\n\n{texto_quadrado}\n\nAposte com {numero_bombas} bombas\n\nEspera ai 2 minutos para a proxima entrada..."

    # Enviar a mensagem para o chat
    await bot.send_message(chat_id=group_id, text=mensagem)

tamanho = 5
num_uns = 4
numero_bombas = random.choice([3, 4])

while True:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(enviar_quadrado_e_mensagem(tamanho, num_uns))

    print("\nEspera ai 7 minutos para a proxima entrada...\n")
    time.sleep(2 * 60)
