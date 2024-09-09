from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def handle_buy(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Купить устройство", callback_data='buy_device'), InlineKeyboardButton("Купить зап/часть", callback_data='buy_parts')],
        [InlineKeyboardButton("В главное меню", callback_data='back')]

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)



    await update.callback_query.edit_message_text('Ты в покупке', reply_markup=reply_markup, parse_mode='Markdown')