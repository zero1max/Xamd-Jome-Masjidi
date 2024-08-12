from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

tel = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Telefon raqamingizni jo'nating!",
    keyboard=[
        [KeyboardButton(text="Telefon raqam jo'natish📱", request_contact=True)]
    ]
)