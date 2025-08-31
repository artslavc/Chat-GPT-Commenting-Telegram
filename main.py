from pyrogram import Client
from datetime import datetime as DT
import time
import asyncio
import sys

from start_thread import start_thread


print("██████╗░██╗░░██╗░█████╗░███╗░░██╗██████╗░██╗░░░██╗  ░██████╗░█████╗░██████╗░██╗██████╗░████████╗")
print("██╔══██╗██║░░██║██╔══██╗████╗░██║██╔══██╗╚██╗░██╔╝  ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝")
print("██████╔╝███████║██║░░██║██╔██╗██║██████╦╝░╚████╔╝░  ╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░")
print("██╔═══╝░██╔══██║██║░░██║██║╚████║██╔══██╗░░╚██╔╝░░  ░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░")
print("██║░░░░░██║░░██║╚█████╔╝██║░╚███║██████╦╝░░░██║░░░  ██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░")
print("╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░")

dt_now = DT.now()
current_date = round(time.time())
date_activation = 'unlimit' # Конец Активации
time_struct = time.localtime(date_activation)
print(f'! Конец Активации: {time_struct.tm_mon}.{time_struct.tm_mday}.{time_struct.tm_year}\n')

# Проверка, есть ли файлы API_ID и API_HASH
try:
    with open(f'API_ID.txt', 'r') as file, open(f'API_HASH.txt', 'r') as file_1:
        API_ID = int(file.read())
        API_HASH = file_1.read()

    try: # channels_id.txt
        with open('channels_id.txt', 'r') as file:
            needs_channels = file.read().split(',')
    except:
        with open('channels_id.txt', 'w') as file:
            file.write('Пример заполнения для channels_id.txt: -10101000100,-10100001010101,1010000001 и т.д.\n'
                       'Этот текст нужно убрать!')
except:
    with open(f'API_ID.txt', 'w') as file, open(f'API_HASH.txt', 'w') as file_1:
        file.write('На сайте https://telegram.org/apps получите API_ID. Введите его сюда вместо этого текста')
        file_1.write('На сайте https://telegram.org/apps получите API_HASH. Введите его сюда вместо этого текста')
    print('Файл API_ID.txt и API_HASH.txt не найдены!\n'
          'Файлы были созданы заново программой.')
    input('\nНажмите ENTER Для Завершения...')
    sys.exit(0)

if date_activation != 'unlimit':
    if current_date > date_activation:
        print('Ваша Подписка Истекла!\n'
              'Напишите в Telegram Для Продления: ')
        input('\nНажмите ENTER Для Завершения...')
        sys.exit(0)

try:
    with open('channels_id.txt', 'r') as file:
        needs_channels = file.read().split(',')
        async def main():
            client = Client('new_session', int(API_ID), API_HASH)
            print(f'Приложение Стартовало: {str(DT.now()).split(".")[0]}')
            print(f'API_ID: {API_ID}\n'
                  f'API_HASH: {API_HASH}\n')

            async with client:
                print("Запускаю обработчик сообщений для всех целевых чатов...")
                await start_thread(client, needs_channels)

        # Запускаем основную функцию асинхронно
        if __name__ == "__main__":
            asyncio.run(main())
except:
    print('* Проверьте правильность заполнения файлов API_ID и API_HASH!\n'
          'Пример заполнения для channels_id.txt: -10101000100,-10100001010101,1010000001 и т.д.')
    input('\nНажмите ENTER Для Завершения...')
