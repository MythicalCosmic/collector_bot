"""
FSM states
"""
from aiogram.fsm.state import State, StatesGroup

class UserStates(StatesGroup):
    """User FSM states"""
    idle = State()