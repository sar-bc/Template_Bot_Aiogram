from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from database.Database import DataBase
from database.models import UserState
# from core.log import Loger
from core.dictionary import *
# import app.keyboards as kb
# import re
# import locale
import logging
from datetime import datetime
from app.state import *
# Установка русской локали
# locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)
# logger = Loger()
# logger.get_name_log(__name__)

user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    logger.info(f'ID_TG:{message.from_user.id}|Команда старт')
    await message.answer(welcom_text)
    # db = DataBase()
    # user_state = await db.get_state(message.from_user.id)
    # await handle_start_command(message, state, user_state)  # Передаем необходимые параметры
    
