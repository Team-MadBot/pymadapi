# Работа с пользователями в PyMadAPI

## Без async/await

### Получить информацию о пользователе

```python
# -*- coding: utf-8 -*-

from pymadapi.base import UserSession


if __name__ == "__main__":
	key = 'your-api-token'
	session = UserSession(key) # Создаёт сессию для работы с пользователями
	user = UserSession.get_userinfo(560529834325966858) # Получаем информацию о пользователе с ID равным 560529834325966858
	print(user) # Выводим краткую информацию о пользователе
``` 

### Обновить уровень подписки MadBot Premium у существующего пользователя
```python
# -*- coding: utf-8 -*-

from pymadapi.base import UserSession


if __name__ == "__main__":
	key = 'your-api-token'
	session = UserSession(key) # Создаёт сессию для работы с пользователями.
	result = UserSession.update_premium_user( # Меняем уровень подписки на 'user' пользователю с ID 560529834325966858
		560529834325966858, 
		level_type='user'
	) 
	print(result) # Выводим True, если всё прошло успешно, иначе мы словим ошибку
```

### Выдать подписку MadBot Premium с определённым уровнем новому пользователю
```python
# -*- coding: utf-8 -*-

from pymadapi.base import UserSession


if __name__ == "__main__":
	key = 'your-api-token'
	session = UserSession(key) # Создаёт сессию для работы с пользователями.
	result = UserSession.set_premium_user( # Выдаём MadBot Premium User пользователю с ID 560529834325966858
		560529834325966858, 
		level_type='user'
	) 
	print(result) # Выводим True, если всё прошло успешно, иначе мы словим ошибку
```

## С использованием async/await

### Получить информацию о пользователе

```python
# -*- coding: utf-8 -*-

import asyncio
from pymadapi.aio import UserSession
# pymadapi.base - не асинхронное обращение к API
# pymadapi.aio - тоже самое, только асинхронное.

async def main():
	key = 'your-api-token'
	session = UserSession(key) # Создаёт сессию для работы с пользователями
	user = await UserSession.get_userinfo(560529834325966858) # Получаем информацию о пользователе с ID равным 560529834325966858
	print(user) # Выводим краткую информацию о пользователе
	await session.close() # Закрываем сессию.

if __name__ == "__main__":
	asyncio.run(main())
``` 

### Обновить уровень подписки MadBot Premium у существующего пользователя
```python
# -*- coding: utf-8 -*-

import asyncio
from pymadapi.aio import UserSession
# pymadapi.base - не асинхронное обращение к API
# pymadapi.aio - тоже самое, только асинхронное.

async def main():
	key = 'your-api-token'
	session = UserSession(key) # Создаёт сессию для работы с пользователями.
	result = await UserSession.update_premium_user( # Меняем уровень подписки на 'user' пользователю с ID 560529834325966858
		560529834325966858, 
		level_type='user'
	) 
	print(result) # Выводим True, если всё прошло успешно, иначе мы словим ошибку
	await session.close() # Закрываем сессию.

if __name__ == "__main__":
	asyncio.run(main())
```

### Выдать подписку MadBot Premium с определённым уровнем новому пользователю
```python
# -*- coding: utf-8 -*-

import asyncio
from pymadapi.aio import UserSession
# pymadapi.base - не асинхронное обращение к API
# pymadapi.aio - тоже самое, только асинхронное.

async def main():
	key = 'your-api-token'
	session = UserSession(key) # Создаёт сессию для работы с пользователями.
	result = await UserSession.set_premium_user( # Выдаём MadBot Premium User пользователю с ID 560529834325966858
		560529834325966858, 
		level_type='user'
	) 
	print(result) # Выводим True, если всё прошло успешно, иначе мы словим ошибку
	await session.close() # Закрываем сессию.

if __name__ == "__main__":
	asyncio.run(main())
```


А всё!
Пока что, больше ничего нету (как и в самом API). В ближайшее время будет добавлено больше возможностей.