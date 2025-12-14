"""
Reply keyboards
"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_reply_keyboard() -> ReplyKeyboardMarkup:
    """Get main reply keyboard"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Option 1")],
            [KeyboardButton(text="Option 2")]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_add_report_keyboard() -> ReplyKeyboardMarkup:
    """Get add report reply keyboard"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Add Report")],
            [KeyboardButton(text="Cancel")]
        ],
        resize_keyboard=True
    )
    return keyboard