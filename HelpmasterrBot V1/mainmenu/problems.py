from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

async def handle_problems(update: Update, context: CallbackContext):
    
    keyboard = [
        [InlineKeyboardButton("📴Не включается", callback_data='no_power') , InlineKeyboardButton("🔋Не заряжается", callback_data='no_charge') ],
        [InlineKeyboardButton("❌Нет сети", callback_data='no_service') , InlineKeyboardButton("🖼️Нет изображения", callback_data='no_image') ],
        [InlineKeyboardButton("📳BootLoop", callback_data='bootloop') , InlineKeyboardButton("🔇Нет звука", callback_data='no_sound') ],
        [InlineKeyboardButton("📢Не работает микрофон ", callback_data='no_mic') , InlineKeyboardButton("Пока что тут пусто", callback_data='back') ],
        [InlineKeyboardButton("🔙 В главное меню", callback_data='back')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.callback_query.edit_message_text('Вы выбрали: Типовые неисправности', reply_markup=reply_markup)
