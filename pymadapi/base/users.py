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

import requests

from pymadapi import BASE_URL
from pymadapi import __version__
from pymadapi.models import User
from pymadapi.models import SubscriptionType
from pymadapi.errors import Forbidden
from pymadapi.errors import Unauthorized
from pymadapi.errors import UserNotFound

class UserSession:
	"""Create a new MadAPI User non-async session.

	Methods
	-------
	get_userinfo(user_id: int)
		Fetch the `User` model with the current `user_id` from MadAPI.
	"""
	def __init__(self, api_key: str):
		"""Init a new UserSession for MadAPI

		Parameters
		----------
		api_key: str
			MadAPI key for access to API.
		"""
		self.api_key = api_key

	def get_userinfo(self, user_id: int) -> User:
		"""Gets userinfo from the MadAPI.

		Parameters
		----------
		user_id: int
			ID of the user.

		Raises
		------
		pymadapi.errors.UserNotFound
			Raises when the user wasn't found.
		pymadapi.errors.Forbidden
			Raises when the access to this method is forbidden.
		pymadapi.errors.Unauthorized
			Raises when your API key is incorrect.

		Returns
		-------
		pymadapi.models.User
			Response with the information about user.
		"""
		response = requests.get(
			BASE_URL + '/user/' + str(user_id), 
			headers = {
				"Authorization": self.api_key
			}
		)
		resp_json = response.json()

		if response.status_code == 401:
			raise Unauthorized("Your API key is incorrect!")
		if response.status_code == 403:
			raise Forbidden("You don't have access to this method!")
		if response.status_code == 404:
			raise UserNotFound(f"The user with ID '{user_id}' wasn't found!")

		return User(
			user_id=int(resp_json['user_id']),
			code=response.status_code,
			is_premium=resp_json['is_premium'],
			type=resp_json['type']
		)