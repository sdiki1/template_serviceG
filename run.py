from silenuem import AccountManager
from DB import engine

if __name__ == "__main__":
    account_manager = AccountManager(engine)
    account_id = account_manager.create_new_account()
