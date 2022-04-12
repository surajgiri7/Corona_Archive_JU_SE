class UnknownError(Exception):
    ''' Raised for unknown errors '''
    message = "Unknown error detected. Please try again"
    
    def __init__(self):
        super().__init__(self.message)
    pass

class DatabaseError(Exception):
    ''' Raised for errors regarding the database conneciton '''
    message = "Unable to connect to the database. Check the server.py file config settings and try again."

    def __init__(self): 
        super().__init__(self.message)
    pass

class LoginError(Exception):
    ''' Raised for errors regarding login issues '''
    message = "Invalid login detected. Please contact your system administrator"
    
    def __init__(self):
        super().__init__(self.message)
    pass

class UserPassNotFound(Exception):
    ''' Raised for errors regarding login issues '''
    message = "Invalid username and/or password"
    
    def __init__(self):
        super().__init__(self.message)
    pass

class UsernameTakenError(Exception):
    ''' Raised if the given username is already in the database '''
    message = "Username taken! Please change it and try again"
    
    def __init__(self):
        super().__init__(self.message)
    pass

class AlreadyInDatabaseError(Exception):
    ''' Raised if the input data is already in the database '''
    message = "Invalid username and/or password"
    
    def __init__(self):
        super().__init__(self.message)
    pass