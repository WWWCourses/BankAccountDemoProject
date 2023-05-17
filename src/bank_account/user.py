from typing import TypeVar, Callable
from bank_account.constants import MENU_OPTIONS
from bank_account.types import AccountDict

T = TypeVar('T', str,int,float)

def get_input_in_range(prompt: str, data_type: Callable[[str], T], min_value: T=None, max_value: T=None) -> T:
	range_info = ""
	if min_value is not None and max_value is not None:
		range_info = f" (Min: {min_value}, Max: {max_value})"

	while True:
		try:
			user_input = data_type(input(prompt + range_info + ": "))

			# check if string input contains only digits, and convert it to int for numerical comparison
			if data_type==str:
				try:
					int(user_input)
				except:
					raise ValueError(f"Input must contains only digits")

			# check for valid range
			if user_input < min_value or user_input > max_value:
				raise ValueError(f"Input must be in range {range_info}")

			return user_input
		except ValueError as e:
			print(f"Invalid input: {e}. Please try again.")
		except KeyboardInterrupt:
			print("\nKeyboardInterrupt detected. Exiting.")
			raise SystemExit
		# except Exception as e:
		# 	print(f"An error occurred: {e}. Please try again.")



def enter_option()->str:
	min = 1
	max = len(MENU_OPTIONS)
	prompt = f'Select an option'

	return get_input_in_range(prompt,int,min,max)


def enter_pin()->str:
	""" Enter valid pin: 4 digits"""
	min = '0000'
	max = '9999'
	prompt = f'Enter PIN'

	return get_input_in_range(prompt,str,min,max)


def enter_account_number()->str:
	""" Enter valid account number"""
	min = '00'
	max = '99'
	prompt = f'Enter account number'

	return get_input_in_range(prompt,str,min,max)


def enter_money_value()->float:
	"""Enter value to deposit|withraw"""

	min = 0
	max = 1_000_000
	prompt = f'Enter amount'
	return get_input_in_range(prompt,float,min,max)


def auth_user(account:AccountDict)->bool:
	pin = enter_pin()

	return True if account['pin']==pin else False