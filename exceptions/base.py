class AppError(Exception):
    """Base class for all exceptions in the application."""
    def __init__(self,message = "An application error occured",code = 500 ):
        self.__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"
    

    def to_dict(self): 
        return { "error": self.__class__.__name__, "message": self.message, "code": self.code }
    


