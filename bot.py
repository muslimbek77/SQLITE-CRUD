import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from baza import create_table,add_user,select_user,count_user,select_all_users_id
from aiogram.fsm.context import FSMContext
from filters.admin import IsBotAdminFilter
#Pastdagi ADMINS ro'yhatiga o'zingizning profil id laringizni qo'yasiz
ADMINS = [7605884028,6134369168]
logging.basicConfig(level=logging.INFO)
bot = Bot(token="Sizning Tokeningiz")
dp = Dispatcher()

from aiogram.fsm.state import StatesGroup, State

class Elon(StatesGroup):
    reklama = State()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    telegram_id = message.from_user.id
    user = select_user(telegram_id)
    full_name = message.from_user.full_name.replace("'","`")
    if not user:
        user_link = message.from_user.mention_html(full_name)
        add_user(telegram_id,full_name,user_link)
        text = f"""Botimizga yangi foydalanuvchi qo'shildi!!!\n{user_link}"""
        await bot.send_message(chat_id=ADMINS[0],text=text,parse_mode="html")

    await message.answer(f"Salom, {full_name}")


@dp.message(Command("count"))
async def foydalanuvchilar_soni(message:types.Message):
    c_users = count_user()
    text = f"Botimizda {c_users}ta foydalanuvchi mavjud..!"
    await message.answer(text)



@dp.message(Command("advert"),IsBotAdminFilter(ADMINS))
async def send_ad_command(message: types.Message, state: FSMContext):
    await message.answer("Reklama yuborishingiz mumkin...")
    await state.set_state(Elon.reklama)

@dp.message(Command("advert"))
async def send_ad_commands(message: types.Message, state: FSMContext):
    await message.answer("Siz Admin emassiz")
    await state.clear()

@dp.message(Elon.reklama)
async def sending_advert(message: types.Message, state: FSMContext):
    await state.clear()
    users = select_all_users_id()
    count = count_user()
        
    for user in users:
        user_id = user[0]
        try:
            await bot.copy_message(user_id, message.chat.id, message.message_id, reply_markup=message.reply_markup)
            await asyncio.sleep(0.05)
        except:
            pass

    await message.answer(f"{count}ta foydalanuvchiga reklama yuborildi.")

async def main():
    create_table()
    await dp.start_polling(bot)
    


if __name__ == "__main__":
    asyncio.run(main())



