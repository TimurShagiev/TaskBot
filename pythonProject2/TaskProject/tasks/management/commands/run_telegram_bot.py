import sqlite3
from django.core.management.base import BaseCommand
import telebot
from tasks.models import Task


bot = telebot.TeleBot("6320700758:AAFxoLeyKsL8e-wE1-yHrZ-pMqbXYJ0VJNI")




@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")


@bot.message_handler(commands=['tasks'])
def tasks(message):
    tasks = Task.objects.all()
    for task in tasks:
        bot.send_message(message.chat.id, "Name: " + task.name + " Importance: " + str(task.importance))

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Список комманд:\n/start - Начать\n/tasks - Список дел\n/help - Список комманд")

@bot.message_handler(commands=['add'])
def add(message):
    # Получаем аргументы команды
    text = message.text[len('/add '):].strip()
    args = text.split()

    # Проверяем, что передано достаточно аргументов
    if len(args) != 2:
        bot.send_message(message.chat.id, 'Вот шаблон, как пользоваться функцией /add:\n /add <имя> <важность(от 1 до 4)>')
        return

    task_name = args[0]
    try:
        importance = int(args[1])
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка: importance должно быть числом от 1 до 4')
        return

    # Проверяем валидность значения importance
    if importance < 1 or importance > 4:
        bot.send_message(message.chat.id, 'Ошибка: importance должно быть числом от 1 до 4')
        return

    new_task = Task.objects.create(name=task_name, importance=importance)

    bot.send_message(message.chat.id, f'Задача "{task_name}" добавлена с важностью {importance}')


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)