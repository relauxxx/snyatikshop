from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def handle_blacklist(update: Update, context: CallbackContext):
    # Кнопка "Назад"
    back_button = [[InlineKeyboardButton("🔙 В главное меню", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(back_button)

    await update.callback_query.edit_message_text('Вы выбрали: Черный список', reply_markup=reply_markup)
