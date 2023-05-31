from bank_account.constants import CURRENCY
from bank_account.types import AccountDict

class Account:
	def __init__(self, id: str="", full_name: str="", pin: str="", balance: float = 0.0):
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

	def convert_to_dict(self)->AccountDict:
		return {
			'balance':self.balance,
			'full_name':self.full_name,
			'pin':self.pin,
			'id':self.id
		}

	def create_from_dict(self, account:AccountDict)->None:
		self.full_name = account['full_name']
		self.balance = account['balance']
		self.id = account['id']
		self.pin = account['pin']


