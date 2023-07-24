import pymongo
from bank_account.types import AccountDict

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["bank_account"]
accounts = db["accounts"]
print('ACCOUNTS:')
print(accounts)

def _get_last_id():
    try:
        db.validate_collection("accounts")
        # last_account = accounts.find({},{"id":1}).sort("id",-1).limit(1)
        last_account = accounts.find_one(sort=[( 'id', pymongo.DESCENDING )])
        return last_account['id']
    except pymongo.errors.OperationFailure:  # If the collection doesn't exist
        print("This collection doesn't exist")
        return 0

def get_accounts():
    return list(accounts.find())

def create_account(account: AccountDict):
    accounts.insert_one(account)

def update_account(account: AccountDict):
    accounts.update_one({"id": account["id"]}, {"$set": account})

def find_account_by_id(account_id: str) -> AccountDict | None:
    return accounts.find_one({"id": account_id})

def show_all_accounts():
    return list(accounts.find({},{"_id":0}))

