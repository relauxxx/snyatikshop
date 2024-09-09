import sys
import os
# Базовая база
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
# Добавляем путь к папке marketfolder
sys.path.append(os.path.abspath("C:/Users/Express Service/Desktop/HelpmasterrBot V1/marketfolder"))
sys.path.append(os.path.abspath("C:/Users/Express Service/Desktop/HelpmasterrBot V1/mainmenu"))     
sys.path.append(os.path.abspath("C:/Users/Express Service/Desktop/HelpmasterrBot V1/typeProblem"))     
# Импортируем код из файлов в папке mainMenu 
from panic import handle_panic
from problems import handle_problems
from services import handle_services
from market import handle_market
from blacklist import handle_blacklist
from delivery import handle_delivery
# Импортируем код из файлов в папке marketfolder 
from buy import handle_buy
from buy_device import handle_buy_device
from buy_parts import handle_buy_parts
from sell import handle_sell
from sell_device import handle_sell_device
from sell_parts import handle_sell_parts
#Имортируем код из файлов в папке typeProblem
from no_charge import handle_no_charge
from no_image import handle_no_image
from no_mic import handle_no_mic
from no_power import handle_no_power
from no_service import handle_no_service
from no_sound import handle_no_sound
from bootloop import handle_bootloop




# Функция для обработки нажатий кнопок
async def handle_button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    # Проверяем, на какую кнопку нажал пользователь
    if query.data == 'panic':
        await handle_panic(update, context)
    elif query.data == 'problems':
        await handle_problems(update, context)
    elif query.data == 'services':
        await handle_services(update, context)
    elif query.data == 'market':
        await handle_market(update, context)
    elif query.data == 'blacklist':
        await handle_blacklist(update, context)
    elif query.data == 'delivery':
        await handle_delivery(update, context)
    elif query.data == 'sell':
        await handle_sell(update, context)
    elif query.data == 'sell_parts':
        await handle_sell_parts(update, context)
    elif query.data == 'sell_device':
        await handle_sell_device(update, context)    
    elif query.data == 'buy':
        await handle_buy(update, context)
    elif query.data == 'buy_device':
        await handle_buy_device(update, context)
    elif query.data == 'buy_parts':
        await handle_buy_parts(update, context)
    elif query.data == 'no_charge':
        await handle_no_charge(update, context)
    elif query.data == 'no_image':
        await handle_no_image(update, context)
    elif query.data == 'no_mic':
        await handle_no_mic(update, context)   
    elif query.data == 'no_power':
        await handle_no_power(update, context)
    elif query.data == 'no_service':
        await handle_no_service(update, context)
    elif query.data == 'no_sound':
        await handle_no_sound(update, context)   
    elif query.data == 'bootloop':
        await handle_bootloop(update, context)    
    elif query.data == 'back':

        # Возвращаемся в главное меню
        keyboard = [
           [InlineKeyboardButton("Panic-Full", callback_data='panic'), InlineKeyboardButton("Типовые неисправности", callback_data='problems')],
            [InlineKeyboardButton("Услуги мастеров", callback_data='services'), InlineKeyboardButton("Рынок", callback_data='market')],
            [InlineKeyboardButton("Курьерские службы", callback_data='delivery'), InlineKeyboardButton("Черный список", callback_data='blacklist')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text('Привет! Я Master Bot. Я помогу вам с ремонтом техники. Выберите, чем могу помочь:', reply_markup=reply_markup)
