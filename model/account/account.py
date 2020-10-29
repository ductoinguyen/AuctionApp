class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def printInfo(self):
        return (self.username + " " + self.password)
        
