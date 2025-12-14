"""
Helper functions
"""

def format_user_mention(user_id: int, name: str) -> str:
    """Format user mention for HTML"""
    return f'<a href="tg://user?id={user_id}">{name}</a>'

def add_user_to_data(data: dict, user_id: int, first_name: str, last_name: str = None, username: str = None) -> None:
    """Add user information to data dictionary"""
    