import bank_account.db as db
from bank_account.types import AccountDict
from bank_account.constants import CURRENCY
import bank_account.user as user




accounts = db.get_accounts()
if not accounts:
	raise Exception('Can not get accounts')


class Account:
	def __init__(self, id: str, full_name: str, pin: str, balance: float = 0.0):
		self.id = id
		self.full_name = full_name
		self.pin = pin
		self.balance = balance

	def withdraw(self, value: float) -> None:
		if value > self.balance:
			print(f"\nNot enough money. You have only {self.balance}")
		else:
			self.balance -= value
			print(f"Successfully withdrawn {value}{CURRENCY}")

	def deposit(self, value: float) -> None:
		self.balance += value
		print(f"Successfully deposited {value}{CURRENCY}")

	def show_details(self) -> None:
		print(f"\nID: {self.id}\nFull Name: {self.full_name}\nBalance: {self.balance}{CURRENCY}")





class BankAccount:
    def __init__(self):
        self.accounts = db.get_accounts()
        if not self.accounts:
            raise Exception('Can not get accounts')

    def _get_last_id(self) -> str:
        return self.accounts[-1]['id']

    def _find_account(self, account_id: str) -> AccountDict | None:
        if self.accounts:
            for acc in self.accounts:
                if acc['id'] == account_id:
                    return acc
        else:
            return None

	def create_new(self)->None:
		""" Creates new bank account"""
		account = Account()
		self.full_name = user.enter_name()
		self.pin = user.enter_pin()
		self.id = f"{int(_get_last_id()) + 1:02}"

		if self.full_name and self.pin:
			print(f"\nYour account is created. Remember your account ID:{id}")
			account:AccountDict = {
				'balance':self.balance,
				'full_name':self.full_name,
				'pin':self.pin,
				'id':self.id
			}
			accounts.append(account)
		else:
			return None




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