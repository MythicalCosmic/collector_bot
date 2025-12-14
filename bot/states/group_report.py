from aiogram.fsm.state import StatesGroup, State


class GroupReportStates(StatesGroup):
    group_name = State()
    group_time = State()
    student_count = State()
    student_present = State()
    student_paid = State()
    exam_day = State()
    confirm_group = State()
