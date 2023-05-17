import bank_account.user as user
import bank_account.account as account

from bank_account.constants import MENU_OPTIONS,LINE_WIDTH

def show_main_menu():
	# print menu header
	print('*'*LINE_WIDTH)
	print(f'***{"Welcome to BankAccount Project":^{LINE_WIDTH-6}s}***')
	print('*'*LINE_WIDTH)
	# print menu options
	for idx,option in enumerate(MENU_OPTIONS):
		print(f'*  {f"{idx+1}. {option}":<{LINE_WIDTH-4}s}*')
	# print menu footer
	print('*'*LINE_WIDTH)


while True :
	show_main_menu()
	option = user.enter_option()

	if option == 1 :
		account.create_new()
	elif option == 2 :
		account.withdraw()
	elif option == 3 :
		account.deposit()
	elif option == 4 :
		account.show_details()
	else : quit()


	# sleep(5)
	# clear_screen()
	# print('test')

