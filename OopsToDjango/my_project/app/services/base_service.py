class BaseService:
    def log(self,message):
        print(f"[LOG] : {message}")

    def validate(self,data):
        if not data:
            raise ValueError("Invalid data provided")
    

    def success_response(self, message):
        return {
            "status": "success",
            "message": message
        }
    
    
    def error_response(self, message):
        return {
            "status": "error",
            "message": message
        }
