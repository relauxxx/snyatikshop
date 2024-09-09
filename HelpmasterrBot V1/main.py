from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext
from handlers import handle_button_click

# Токен твоего бота
TOKEN = '7504376217:AAEOfr0CphGI2sXlfqDoIPNvWR3tIU7tepE'

# Функция приветствия с кнопками
async def start(update: Update, context: CallbackContext):
    # Создаём кнопки в 2 столбца
    keyboard = [
        [InlineKeyboardButton("Panic-Full", callback_data='panic'), InlineKeyboardButton("Типовые неисправности", callback_data='problems')],
        [InlineKeyboardButton("Услуги мастеров", callback_data='services'), InlineKeyboardButton("Рынок", callback_data='market')],
        [InlineKeyboardButton("Курьерские службы", callback_data='delivery'), InlineKeyboardButton("Черный список", callback_data='blacklist')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Приветственное сообщение с предложением помощи
    await update.message.reply_text(
        'Привет! Я Master Bot. Я помогу вам с ремонтом техники. Выберите, чем могу помочь:',
        reply_markup=reply_markup
    )

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Обрабатываем команду /start
    application.add_handler(CommandHandler('start', start))

    # Обрабатываем нажатия на кнопки
    application.add_handler(CallbackQueryHandler(handle_button_click))

    application.run_polling()

if __name__ == '__main__':
    main()
