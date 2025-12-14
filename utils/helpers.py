from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.user import User

async def get_user_by_id(
    session: AsyncSession,
    user_id: int,
) -> User | None:
    result = await session.execute(
        select(User).where(User.id == user_id)
    )
    return result.scalar_one_or_none()


async def create_user(
    session: AsyncSession,
    tg_user,
) -> User:
    user = User(
        id=tg_user.id,
        first_name=tg_user.first_name,
        last_name=tg_user.last_name,
        username=tg_user.username,
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user


async def get_or_create_user(
    session: AsyncSession,
    tg_user,
) -> User:
    user = await get_user_by_id(session, tg_user.id)
    if user:
        return user

    return await create_user(session, tg_user)
