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

class SubscriptionType:
	"""Subscription level class"""
	
	def __init__(self, _type: str):
		"""Init a new SubscriptionType class

		Parameters
		----------
		server: bool
			Checks if the subscription type is Server
		user: bool
			Checks if the subscription type is User
		"""
		self.server = _type == "server"
		self.user = _type == "user"

	def __repr__(self):
		return f"<SubscriptionType 'user': {self.user}, 'server': {self.server}>"

class User:
	"""`get_userinfo` API method response"""

	def __init__(self, *args, **kwargs):
		"""Init a new User class.

		Parameters
		----------
		user_id: int
			User ID.
		code: int
			Status code for current API response.
		is_premium: bool
			Fast check if the user has MadBot Premium Server or User subscription.
		type: SubscriptionType
			The type of subscription of the user.
		"""
		self.user_id = int(kwargs.pop('user_id'))
		self.code = kwargs.pop('code')
		self.is_premium = kwargs.pop('is_premium')
		self.type = SubscriptionType(_type=kwargs.pop('type'))

	def __repr__(self):
		return f"<User[{self.code}] ID: {self.user_id}, is_premium: '{self.is_premium}', type: '{self.type}'>"

	def __int__(self):
		return self.user_id

	def __bool__(self):
		return self.is_premium