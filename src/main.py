from bank_account.constants import MENU_OPTIONS,LINE_WIDTH
from bank_account.bank import Bank
import bank_account.user as user

def show_header(prompt:str)->None:
	# print menu header
	print()
	print('*'*LINE_WIDTH)
	print(f'***{f"{prompt}":^{LINE_WIDTH-6}s}***')
	print('*'*LINE_WIDTH)

def show_main_menu():
	show_header('Welcome to BankAccount Project')
	# print menu options
	for idx,option in enumerate(MENU_OPTIONS):
		print(f'*  {f"{idx+1}. {option}":<{LINE_WIDTH-4}s}*')
	# print menu footer
	print('*'*LINE_WIDTH)


# create new bank to operate on
bank = Bank()

while True :
	show_main_menu()
	option = user.enter_option()

	if option == '1' :
		show_header('Create new account')
		bank.create_new_account()
	elif option == '2' :
		show_header('Withdraw')
		bank.withdraw()
	elif option == '3' :
		show_header('Deposit')
		bank.deposit()
	elif option == '4' :
		show_header('Account Details')
		bank.show_account_details()
	elif option == '5' :
		show_header('Show All Accounts')
		bank.show_all_accounts()
	else : quit()


	# sleep(5)
	# clear_screen()
	# print('test')

