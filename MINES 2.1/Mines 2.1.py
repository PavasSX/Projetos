import random
import time
import telegram
import asyncio


tamanho = 5
num_uns = 4
numero_bombas = random.choice([3, 4]) 


bot_token = 'TOKEN DO SEU BOT TELEGRAM'


bot = telegram.Bot(token=bot_token)


group_id = 'ID DO GRUPO'

async def enviar_quadrado_e_mensagem(tamanho, num_uns):
    if num_uns > tamanho ** 2:
        raise ValueError(f"Erro: O número de bombas ({num_uns}) excede o tamanho do quadrado ({tamanho}x{tamanho}). O número máximo de bombas permitido é {tamanho ** 2}.")

    quadrado = [['💣' for _ in range(tamanho)] for _ in range(tamanho)]

    posicoes = [(i, j) for i in range(tamanho) for j in range(tamanho)]
    random.shuffle(posicoes)

    for i in range(num_uns):
        linha, coluna = posicoes[i]
        quadrado[linha][coluna] = '💎'

    
    texto_quadrado = '\n'.join([' '.join(map(str, linha)) for linha in quadrado])

    
    mensagem = f"Bem vindo ao Mines!\n\npelo menos duas tentativas\n\n{texto_quadrado}\n\nAposte com {numero_bombas} bombas\n\nEspere 2 minutos para a proxima entrada..."

    
    await bot.send_message(chat_id=group_id, text=mensagem)



while True:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(enviar_quadrado_e_mensagem(tamanho, num_uns))

    print("\nCódigo está funcionando, confira seu grupo no telegram.\n")
    
    time.sleep(2 * 60)
