"""
Message handlers
"""
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.states.group_report import GroupReportStates
from i18n.i18n import I18nText
from bot.keyboards.reply import get_add_report_keyboard
from i18n.i18n import t

router = Router()


@router.message(I18nText("buttons.add_report"))
async def start_report(
    message: Message,
    state: FSMContext,
    user,
    session
):
    await state.set_state(GroupReportStates.report_group_count)

    await message.answer(
        t(user.lang, "messages.start_report")
    )


@router.message()
async def echo_message(message: Message):
    """Echo all text messages"""
    await message.answer(f"You said: {message.text}", reply_markup=get_add_report_keyboard())