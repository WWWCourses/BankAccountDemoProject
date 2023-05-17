from typing import Callable, TypeVar

T = TypeVar('T', int, float, str)

def get_user_input(prompt: str, data_type: Callable[[str], T], min_value: T=None, max_value: T=None) -> T:
	range_info = ""
	if min_value is not None and max_value is not None:
		range_info = f" (Min: {min_value}, Max: {max_value})"

	while True:
		try:
			user_input = data_type(input(prompt + range_info + ": "))
			# check if string input contains only digits:
			if data_type==str:
				try:
					int(user_input)
				except:
					raise ValueError(f"Input must be in range {range_info}")


			if user_input < min_value or user_input > max_value:
				raise ValueError(f"Input must be in range {range_info}")

			return user_input
		except ValueError as e:
			print(f"Invalid input: {e}. Please try again.")
		except KeyboardInterrupt:
			print("\nKeyboardInterrupt detected. Exiting.")
			raise SystemExit
		except Exception as e:
			print(f"An error occurred: {e}. Please try again.")


money: float = get_user_input("Enter the amount of money", float, min_value=0, max_value=1_000_000)
print(f"Money: {money}")

pin: str = get_user_input("Enter the PIN", str, min_value='0001', max_value='9999')
print(f"PIN: {pin}")

account_number: str = get_user_input("Enter the account number", str, min_value='01', max_value='99')
print(f"Account Number: {account_number}")
