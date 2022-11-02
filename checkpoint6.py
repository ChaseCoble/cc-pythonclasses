class User:

    def __init__(self, username, password, passwordconfirm):
        self.username = username
        self.password = password
        self.passwordconfirm = passwordconfirm
    def __passwordvalidation__(self, password, passwordconfirm):
        if password == passwordconfirm:
            password = passwordconfirm
        elif password != passwordconfirm:
            print("Password doesn't match")
            return ("Failure")
        else:
            print('Error')
authUser = User('DravenDraegos', 'Fubar2', 'Fubar2')
print = User.__passwordvalidation__
   
