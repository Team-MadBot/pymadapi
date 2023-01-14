# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2023 MadCat9958
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

class MadAPIError(BaseException):
	"""Base exception class than represents MadAPI errors"""

class UserNotFound(MadAPIError):
	"""Exception that raises when given user wasn't found"""

class Unauthorized(MadAPIError):
	"""Exception that raises when given API key is incorrect"""

class Forbidden(MadAPIError):
	"""Exception that raises when given API key hasn't permissions for using the method"""

class BadRequest(MadAPIError):
	"""Exception that raises when given argument is incorrect"""