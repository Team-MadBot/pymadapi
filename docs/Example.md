# Работа с пользователями в PyMadAPI

### Получить информацию о пользователе

```python
# -*- coding: utf-8 -*-

from pymadapi.base import UserSession


if __name__ == "__main__":
	key = 'your-api-token'
	session = UserSession(key) # Создаёт сессию для работы с пользователями
	user = UserSession.get_userinfo(560529834325966858) # Получаем информацию о пользователе с 
														# ID равным 560529834325966858
	print(user) # Выводим краткую информацию о пользователе
``` 

А всё!
Пока что, больше ничего нету (как и в самом API). В ближайшее время будет добавлено больше возможностей.