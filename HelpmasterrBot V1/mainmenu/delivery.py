from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def handle_delivery(update: Update, context: CallbackContext):
    # Кнопка "Назад"
    back_button = [[InlineKeyboardButton("🔙 В главное меню", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(back_button)

    delivery_message = (
       '1.Курьерская служба "Изи доставка" - @ez\\_dostavka\n'
           ' Первая доставка бесплатно\n'
            ' Выкуп без ограничений,возят по всему городу ,множество доставок каждый день,быстрее чем достависта\n'

        ' \n'
        

       '2.Курерская служба "Туда-сюда курьер" - @Sam\\_sebe\\_programist'
    )

    await update.callback_query.edit_message_text(delivery_message, reply_markup=reply_markup, parse_mode='Markdown')