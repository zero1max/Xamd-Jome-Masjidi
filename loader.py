from aiogram import Dispatcher , Router, Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from database.users_db import Database_Users

TOKEN = "YOUR_BOT_TOKEN"

dp = Dispatcher()
router_admin = Router()
router = Router()
db_users = Database_Users()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp.include_router(router=router_admin)
dp.include_router(router=router)
