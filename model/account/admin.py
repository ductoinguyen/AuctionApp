import model.account.account as account
class Admin(account.Account):
    def __init__(self, username, password):
        super().__init__(username, password)
    