from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


# Функция для обработки кнопки "Не заряжайки"
async def handle_no_charge(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton('Apple', callback_data='handle_apple_no_charge')],
        [InlineKeyboardButton("В главное меню", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопками
    await update.callback_query.edit_message_text('Не заряжайки', reply_markup=reply_markup, parse_mode='Markdown')



 