from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def handle_sell_device(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("В главное меню", callback_data='back')]

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)



    await update.callback_query.edit_message_text('Ты в продаже устройства', reply_markup=reply_markup, parse_mode='Markdown')