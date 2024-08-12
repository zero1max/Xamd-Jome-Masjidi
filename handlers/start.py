from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from loader import router, bot, db_users
from keyboards.defoult.keys import *

class Users(StatesGroup):
    user_id = State()
    user_nikname = State()
    user_xatm_number = State()

@router.message(CommandStart())
async def start(msg: Message, state: FSMContext):
    await msg.answer("АССАЛОМУ АЛАЙКУМ ВА РАҲМАТУЛЛОҲИ ВА БАРАКАТУҲ!")
    db_users.create_table()
    await state.set_state(Users.user_xatm_number)
    await msg.answer("НEЧТА  ХАТМ ҚИЛГАН БЎЛСАНГИЗ СОНИНИ  ЁЗИБ ҚОЛДИРИНГ!")

@router.message(Users.user_xatm_number)
async def user_xatm_number(msg: Message, state: FSMContext):
    await state.update_data(user_xatm_number=msg.text)
    data = await state.get_data()
    print(data)
    user_id = msg.from_user.id
    user_nikname = msg.from_user.username
    user_xatm_number = data.get('user_xatm_number')

    db_users.add_users(user_id, user_nikname, user_xatm_number)
    await msg.answer("МашаАллоҳ, Аллоҳ қабул қилсин рўйхатга сизни ҳам қўшиб қойдик.")
    await state.clear()


@router.message(Command("id"))
async def id(msg: Message):
    await msg.answer(f"ID: {msg.from_user.id}")