from typing import TypedDict
from bank_account.db import accounts
from bank_account.exceptions import NonExistentAccount,NotEnoughMoney
from bank_account.types import AccountDict
import bank_account.user as user

def get_pin():
	pass

def get_account()->AccountDict|None:
	account_number = user.enter_account_number()

	for acc in accounts:
		if acc['number']==account_number:
			return acc

	raise NonExistentAccount(account_number)


def create_new()->AccountDict:
	""" Creates new bank account"""

def withdraw()->None:
	""" Withdraw money from account"""

	account:AccountDict|None = None
	try:
		account:AccountDict = get_account()
	except NonExistentAccount as e:
		print(e)

	if user.auth_user(account):
		value = user.enter_money_value()
		if value>account['balance']:
			raise NotEnoughMoney(account['balance'])

		account['balance'] -=value

def deposit():
	""" Deposit money into account"""

	account:AccountDict|None = None
	try:
		account:AccountDict = get_account()
	except NonExistentAccount as e:
		print(e)

	if user.auth_user(account):
		account['balance'] +=value

def show_details():
	"""Show Account Details"""

	account:AccountDict|None = None
	try:
		account:AccountDict = get_account()
	except NonExistentAccount as e:
		print(e)

	if user.auth_user(account):
		print(account)