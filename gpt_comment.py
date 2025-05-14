import random
from g4f.client import Client

gpt_client = Client()
old_msg = 0
async def get_neuro_comment(message_text):
    global old_msg
    if old_msg != message_text and len(message_text.split()) > 4:
        old_msg = message_text
        if random.randint(1, 2) == 1:
            response = gpt_client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": f"Привет, ChatGPT. У меня есть пост, и мне нужно, чтобы ты стал диванным экспертом и написал комментарий к этому посту. Можешь допускать ошибки. Прояви свою критику, но без чрезмерных эмоций. Можешь использовать сленг, а быть чуть грубоватым – но в рамках разумного. Главное – звучать как настоящий живой человек, а не как бот. Без кавычек и т.п. Используй максимум 11 слов Вот пост для комментария: '{message_text}'"}]
            )
        else:
            response = gpt_client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user",
                           "content": f"Привет, ChatGPT. Пиши с маленькой буквы. Используй легкую форму матов. У меня есть пост, и мне нужно, чтобы ты стал диванным экспертом и написал комментарий к этому посту. Можешь допускать ошибки. Прояви свою критику, но без чрезмерных эмоций. Можешь использовать сленг, а быть чуть грубоватым – но в рамках разумного. Главное – звучать как настоящий живой человек, а не как бот. Без кавычек и т.п. Используй максимум 11 слов Вот пост для комментария: '{message_text}'"}]
            )
        return response.choices[0].message.content
    else:
        return 0