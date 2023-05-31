import bank_account.db as db
import bank_account.user as user
from bank_account.types import AccountDict
from bank_account.account import Account

class Bank:
	def __init__(self)->None:
		try:
			self.accounts = db.get_accounts() or []
		except Exception as e:
			print('Can not get accounts')
			exit(0)

	def _get_last_id(self) -> str:
		return self.accounts[-1]['id']

	def _find_account(self, account_id: str) -> AccountDict | None:
		for acc in self.accounts:
			if acc['id'] == account_id:
				return acc

		return None

	def get_account(self)->AccountDict|None:
		max_tries = 3
		account:AccountDict|None

		while max_tries:
			account_id = user.enter_account_id()
			account = self._find_account(account_id)

			if account:
				return account
			else:
				print(f"Account ({account_id}) did not exists. Try another id")
				max_tries-=1;

		return None

	def create_new_account(self)->None:
		""" Creates new bank account"""

		full_name = user.enter_name()
		pin = user.enter_pin()
		id = f"{int(self._get_last_id()) + 1:02}"

		if full_name and pin:
			print(f"\nYour account is created. Remember your account ID:{id}")
			account = Account(full_name=full_name, pin=pin, id=id)

			self.accounts.append(account.convert_to_dict())
		else:
			return None

	def withdraw(self)->None:
		# get account
		account:AccountDict|None = self.get_account()
		if not account:
			print('Can not withdraw from non existent account')
			return None

		# auth_user
		if not user.auth_user(account):
			print('\nWrong pin')
			return None

		# get value to withdraw
		value = user.enter_money_value()

		account_obj = Account()
		account_obj.create_from_dict(account)
		account_obj.withdraw(value)

	def deposit(self)->None:
		print(deposit)

	def	show_account_details(self)->None:
		print('show_account_details')

