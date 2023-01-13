# PyMadAPI - MadAPI Python Library
PyMadAPI is easy-to-use library that uses MadAPI. 

# Installing (requires Git)

```bash
$ pip install -U git+https://github.com/Team-MadBot/pymadapi 
```

# Basic usage
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymadapi.base import UserSession


if __name__ == '__main__':
    key = 'your-api-token'
    session = UserSession(key) # Create a session to get userinfo
    user = session.get_userinfo(560529834325966858) # get the user with the `560529834325966858` ID
    print(user.is_premium) # display if the user has a MadBot Premium subscription
```

# License

```
MIT License

Copyright (c) 2023 MadCat9958

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
