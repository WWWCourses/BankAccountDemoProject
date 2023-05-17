class WrongUserInput(Exception):
	def __init__(self, message:str="Error :WrongUserInput") -> None:
		super().__init__(message)


class NonExistentAccount(Exception):
	def __init__(self, account_number) -> None:
		self.message = f"Account doesn't exists [{account_number}]"
		super().__init__(self.message)

class NotEnoughMoney(Exception):
	def __init__(self, balance) -> None:
		self.message = f"Not enough money. Current balance: [{balance}]"
		super().__init__(self.message)

