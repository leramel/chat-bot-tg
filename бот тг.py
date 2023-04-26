from telegram.ext import Application, MessageHandler, filters


BOT_TOKEN = '5638308159:AAG8MzNKwxNyrc4fH_uJ-2GAK1jFe0RCyHs'

async def echo(update, context):

    await update.message.reply_text(f'Я получил сообщение <{update.message.text}>')


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()