from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def handle_buy_parts(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("В главное меню", callback_data='back')]

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)



    await update.callback_query.edit_message_text('Ты в покупке запчастей', reply_markup=reply_markup, parse_mode='Markdown')