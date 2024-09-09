from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def handle_market(update: Update, context: CallbackContext):
    
    # Кнопка "Назад"
    keyboard = [
        [InlineKeyboardButton("Купить", callback_data='buy'), InlineKeyboardButton("Продать", callback_data='sell')],
        [InlineKeyboardButton("В главное меню", callback_data='back')]

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.callback_query.edit_message_text('Вы выбрали: Рынок', reply_markup=reply_markup)
