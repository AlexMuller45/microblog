""" Модуль для заполнения БД произвольными данными"""

import asyncio
import json
from typing import List

import aiohttp

from core.models import User

URL_user: str = "https://random-data-api.com/api/users/random_user"


async def get_data(url) -> str | None:
    """Получение произвольных данных по заданному URL"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            return await response.text()


async def get_users() -> List[User]:
    """Запись данных в БД"""
    user_tasks = []
    for _ in range(10):
        user_tasks.append(get_data(URL_user))

    user_response = await asyncio.gather(*user_tasks)
    users_data = []
    for response in user_response:
        if response:
            data = json.loads(response)
            users_data.append(User(name=data["username"], api_key=data["password"]))
    return users_data
