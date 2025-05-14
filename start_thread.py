from pyrogram import Client, idle, filters
from pyrogram.types import Message
from datetime import datetime as DT
from pyrogram.handlers import MessageHandler
import asyncio
import random

from gpt_comment import get_neuro_comment

async def handle_poll_message(client, message):
    await asyncio.sleep(random.randint(6, 60))

    disc_msg = await client.get_discussion_message(message.chat.id, message.id)
    question_with_options = message.poll.question + ' ' + ' '.join(option.text for option in message.poll.options)
    if len(message.poll.question.split()) > 4 and '?' in message.poll.question:
        comment_to_post = await get_neuro_comment(question_with_options)
        await disc_msg.reply(comment_to_post)
        print(f'! Опубликовал Комментарий: {comment_to_post} ({str(DT.now()).split(".")[0]}) - ({message.chat.title})')

        if random.randint(1, 5) == 1: # Ставит реакцию или нет
            await asyncio.sleep(random.randint(1, 4))
            async for message in client.get_discussion_replies(message.chat.id, message.id):
                if message.text == comment_to_post:
                    id_msg = message.id
                    list_reactions = ['👍', '❤️']
                    await client.send_reaction(message.chat.id, id_msg, random.choice(list_reactions))
                    break
            print('! Поставил реакцию под комментарий')

async def handle_media_message(client, message):
    await asyncio.sleep(random.randint(6, 60))

    media_message = await client.get_discussion_message(message.chat.id, message.id)
    comment_to_post = await get_neuro_comment(message.caption.replace('\n', ' '))
    if comment_to_post != 0:
        await media_message.reply(comment_to_post)
        print(f'! Опубликовал Комментарий: {comment_to_post} ({str(DT.now()).split(".")[0]}) - ({message.chat.title})')

        if random.randint(1, 5) == 1: # Ставит реакцию или нет
            await asyncio.sleep(random.randint(1, 4))
            async for message in client.get_discussion_replies(message.chat.id, message.id):
                if message.text == comment_to_post:
                    id_msg = message.id
                    list_reactions = ['👍', '❤️']
                    await client.send_reaction(message.chat.id, id_msg, random.choice(list_reactions))
                    break
            print('! Поставил реакцию под комментарий')

async def handle_media_group_message(client, message):
    await asyncio.sleep(random.randint(6, 60))
    
    media_group = await client.get_media_group(message.chat.id, message.id)
    disc_msg = await client.get_discussion_message(message.chat.id, media_group[0].id)
    captions = [media_item.caption for media_item in media_group if media_item.caption]
    all_captions = " ".join(captions)
    comment_to_post = await get_neuro_comment(all_captions.replace('\n', ' ')) if captions else None
    if comment_to_post and comment_to_post != 0:
        await disc_msg.reply(comment_to_post)
        print(f'! Опубликовал Комментарий: {comment_to_post} ({str(DT.now()).split(".")[0]}) - ({message.chat.title})')

        if random.randint(1, 5) == 1: # Ставит реакцию или нет
            await asyncio.sleep(random.randint(1, 4))
            async for message in client.get_discussion_replies(message.chat.id, message.id):
                if message.text == comment_to_post:
                    id_msg = message.id
                    list_reactions = ['👍', '❤️']
                    await client.send_reaction(message.chat.id, id_msg, random.choice(list_reactions))
                    break
            print('! Поставил реакцию под комментарий')

async def handle_text_message(client, message):
    await asyncio.sleep(random.randint(6, 60))

    discussion_message = await client.get_discussion_message(message.chat.id, message.id)
    comment_to_post = await get_neuro_comment(message.text.replace('\n', ' '))

    if comment_to_post != 0:
        await discussion_message.reply(comment_to_post)
        print(f'! Опубликовал Комментарий: {comment_to_post} ({str(DT.now()).split(".")[0]}) - ({message.chat.title})')

        if random.randint(1, 5) == 1: # Ставит реакцию или нет
            await asyncio.sleep(random.randint(1, 4))
            async for message in client.get_discussion_replies(message.chat.id, message.id):
                if message.text == comment_to_post:
                    id_msg = message.id
                    list_reactions = ['👍', '❤️']
                    await client.send_reaction(message.chat.id, id_msg, random.choice(list_reactions))
                    break
            print('! Поставил реакцию под комментарий')

async def my_handler(client: Client, message: Message):
    try:
        if message.poll and random.choice([True, True, True, False]):
            await handle_poll_message(client, message)
        elif message.media and random.choice([True, True, True, False]):
            await handle_media_message(client, message)
        elif message.media_group_id and random.choice([True, True, True, False]):
            await handle_media_group_message(client, message)
        elif message.text and random.choice([True, True, True, False]):
            await handle_text_message(client, message)
    except Exception as e:
        pass

async def start_thread(client, target_channels):
    for channel_id in target_channels:
        if '\n' in channel_id or ' ' in channel_id:
            channel_id = channel_id.replace('\n', ''); channel_id = channel_id.replace(' ', '')
        client.add_handler(MessageHandler(my_handler, filters.chat(int(channel_id))))
    await idle()