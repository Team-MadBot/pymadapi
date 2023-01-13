# Катерогии документации

* [Ошибки](#pymadapi.errors)
  	* [MadAPIError](#pymadapi.errors.MadAPIError)
  	* [UserNotFound](#pymadapi.errors.UserNotFound)
  	* [Unauthozired](#pymadapi.errors.Unauthorized)
  	* [Forbidden](#pymadapi.errors.Forbidden)
* [Модели](#pymadapi.models)
  	* [User](#pymadapi.models.User)
  	* [SubscriptionType](#pymadapi.models.SubscriptionType)
* [Пользователи](#pymadapi.base.users)
  	* [UserSession](#pymadapi.base.users.UserSession)
  		* [get_userinfo](#pymadapi.base.users.get_userinfo)

<a name="pymadapi.errors"></a>
# Ошибки

<a name="pymadapi.errors.MadAPIError"></a>
## MadAPIError

`BaseException` класс, который указывает на ошибки PyMadAPI (или MadAPI).

<a name="pymadapi.errors.UserNotFound"></a>
## UserNotFound

`MadAPIError` класс, который вызывается, если пользователь не обнаружен.

<a name="pymadapi.errors.Unauthozired"></a>
## Unauthozired

`MadAPIError` класс, который вызывается при некорректном токене.

<a name="pymadapi.errors.Forbidden"></a>
## Forbidden

`MadAPIError` класс, который вызывается при отсутствии прав на совершения действия.

<a name="pymadapi.models"></a>
# Модели

<a name="pymadapi.models.User"></a>
## User `(user_id: int, code: int, is_premium: bool, type: str = ['None', 'user', 'server'])`

Класс `User`, который возвращает [`UserSession.get_userinfo`](#pymadapi.base.users.get_userinfo).

Параметры:
---------
- `user_id`: `int` - ID пользователя.
- `code`: `int` - Статус-код запроса информации о пользователе.
- `is_premium`: `bool` - Быстрая проверка на наличие **купленной** подписки MadBot Premium.
- `type`: [`SubscriptionType`](#pymadapi.models.SubscriptionType) - Тип подписки MadBot Premium.


<a name="pymadapi.models.SubscriptionType"></a>
## SubscriptionType `(_type: str = ['None', 'user', 'server'])`

Класс `SubscriptionType`, который содержит информацию о типе подписки MadBot Premium.

Параметры:
----------
- `user`: `bool` - Указывает, имеется ли подписка MadBot Premium User.
- `server`: `bool` - Указывает, имеется ли подписка MadBot Premium Server.

<a name="pymadapi.base.users"></a>
# Работа с пользователями

<a name="pymadapi.base.users.UserSession"></a>
## UserSession `(api_key: str)`

Класс сессии работы с пользователями. Требует для ввода `api_key`.

Параметры:
----------
- `api_key`: `str` - Токен доступа для MadAPI.

Функции:
--------

### - `get_userinfo(user_id: int)`
  Функция для получения информации о пользователе.

  Параметры:
  ----------
  - `user_id`: `int` - ID пользователя.

  Возвращает:
  -----------
  - [`User`](#pymadapi.models.User) - информация о пользователе

  Ошибки:
  -------
  - [`Unauthorized`](#pymadapi.errors.Unauthorized) - вызывается при некорректности токена.
  - [`Forbidden`](#pymadapi.errors.Forbidden) - вызывается при отсутствии доступа к функции.
  - [`UserNotFound`](#pymadapi.errors.UserNotFound) - вызывается при отсутствии указанного пользователя в базе данных API.