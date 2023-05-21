import bank_account.db as db
from bank_account.types import AccountDict
from bank_account.constants import CURRENCY
import bank_account.user as user


accounts = db.get_accounts()
if not accounts:
	raise Exception('Can not get accounts')

def _get_last_id()->str:
	return accounts[-1]['id']

def _find_account(account_id:str)->AccountDict|None:
	if accounts:
		for acc in accounts:
			if acc['id']==account_id:
				return acc
	else:
		return None

def get_account()->AccountDict|None:
	max_tries = 3
	account:AccountDict|None

	while max_tries:
		account_id = user.enter_account_id()
		account = _find_account(account_id)

		if account:
			return account
		else:
			print(f"Account ({account_id}) did not exists.")
			max_tries-=1;

	return None


def create_new()->AccountDict|None:
	""" Creates new bank account"""
	user_name = user.enter_name()
	pin = user.enter_pin()
	id = f"{int(_get_last_id()) + 1:02}"

	if user_name and pin:
		print(f"\nYour account is created. Remember your account ID:{id}")
		account:AccountDict = {
			'balance':0,
			'full_name':user_name,
			'pin':pin,
			'id':id
		}
		accounts.append(account)
	else:
		return None


def withdraw()->None:
	""" Withdraw money from account"""
	# get account
	account:AccountDict|None = get_account()

	if not account:
		print('\nNon existent account')
		return None

	# auth_user
	if not user.auth_user(account):
		print('\nWrong pin')
		return None

	value = user.enter_money_value()

	if value>account['balance']:
		print(f"\nNot enough money. You have only {account['balance']}")
		return None

	account['balance'] -=value
	print(f"Successfully withdrawn {value}{CURRENCY}")

def deposit():
	""" Deposit money into account"""

	# get account
	account:AccountDict|None = get_account()

	if not account:
		print('\nNon existent account')
		return None

	# auth_user
	if not user.auth_user(account):
		print('\nWrong pin')
		return None

	value = user.enter_money_value()
	account['balance'] +=value
	print(f"Successfully deposited {value}{CURRENCY}")


def show_details():
	"""Show Account Details"""

	# get account
	account:AccountDict|None = get_account()

	if not account:
		print('\nNon existent account')
		return None

	# auth_user
	if not user.auth_user(account):
		print('\nWrong pin')
		return None

	print(f"\n{account}")