import bank_account.user as user
import bank_account.account as account

from bank_account.constants import MENU_OPTIONS,LINE_WIDTH

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


while True :
	show_main_menu()
	option = user.enter_option()

	if option == '1' :
		show_header('Create new account')
		account.create_new()
	elif option == '2' :
		show_header('Withdraw')
		account.withdraw()
	elif option == '3' :
		show_header('Deposit')
		account.deposit()
	elif option == '4' :
		show_header('Account Details')
		account.show_details()
	else : quit()


	# sleep(5)
	# clear_screen()
	# print('test')

