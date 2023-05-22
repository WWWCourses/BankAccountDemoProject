from bank_account.types import AccountDict

def get_accounts()->list[AccountDict]|None:
    return [
        {
            'id' : '01',
            'full_name' : 'Даниел Йорданов',
            'pin' : '0001',
            'balance' : 1000
        },
        {
            'id' : '02',
            'full_name' : 'Петър Петров',
            'pin' : '0002',
            'balance' : 2000
        },
        {
            'id': '03',
            'full_name': 'Атанас Кръстев',
            'pin': '0003',
            'balance': 3000
        },
        {
            'id': '04',
            'full_name': 'Иван Стоянов',
            'pin': '0004',
            'balance': 4000
        },
        {
            'id': '05',
            'full_name': 'Валентин Кондев',
            'pin': '0005',
            'balance': 5000
        }
    ]