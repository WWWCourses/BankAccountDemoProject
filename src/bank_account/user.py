from bank_account.constants import MENU_OPTIONS
from bank_account.types import AccountDict

def get_input_in_range_as_float(
	prompt:str,
	min_value:float,
	max_value:float
	)->float:

	range_info = f"[Min: {min_value}, Max: {max_value}]"
	while True:
		try:
			user_input = float(input(f'{prompt} {range_info}: '))
			# validate range
			if user_input < min_value or user_input > max_value:
				raise ValueError(f"Input must be in range {range_info}")

			return user_input
		except ValueError as e:
			print(f"{e}. Please try again.")
		except KeyboardInterrupt:
			print("\nKeyboardInterrupt detected. Exiting.")
			raise SystemExit

def get_input_in_range_as_str(
	prompt: str,
	min_value: str,
	max_value: str
	) -> str:

	range_info = f"[Min: {min_value}, Max: {max_value}]"
	max_value_length = len(max_value)

	while True:
		try:
			user_input = input(f'{prompt} {range_info}: ')

			# check for valid symbols length:
			if len(user_input)!=max_value_length:
				raise ValueError(f"Enter exactly {max_value_length} digits")

			#convert input to int, in order to check if input contains only digits and to compare numbers later
			try:
				user_input_as_int = int(user_input)
			except ValueError:
				raise ValueError(f"Enter digits only")

			# convert range values to int, in order to compare numbers later
			min_value_num = int(min_value)
			max_value_num = int(max_value)

			# validate range
			if user_input_as_int < min_value_num or user_input_as_int > max_value_num:
				raise ValueError(f"Input must be in range {range_info}")

			return user_input
		except ValueError as e:
			print(f"{e}. Please try again.")
		except KeyboardInterrupt:
			print("\nKeyboardInterrupt detected. Exiting.")
			raise SystemExit

def enter_name():
	return  input('Enter your name: ')

def enter_option()->str:
	min = '1'
	max = str(len(MENU_OPTIONS))
	prompt = f'Select an option'

	return get_input_in_range_as_str(prompt,min,max)

def enter_pin()->str:
	""" Enter valid pin: 4 digits"""
	min = '0000'
	max = '9999'
	prompt = f'Enter PIN'

	return get_input_in_range_as_str(prompt,min,max)

def enter_account_id()->str:
	""" Enter valid account number"""
	min = '00'
	max = '99'
	prompt = f'Enter account number'

	return get_input_in_range_as_str(prompt,min,max)

def enter_money_value()->float:
	"""Enter value to deposit|withdraw"""

	min = 0
	max = 1_000_000
	prompt = f'Enter amount'
	return get_input_in_range_as_float(prompt,min,max)

def auth_user(account:AccountDict)->bool:
	pin = enter_pin()

	return True if account['pin']==pin else False