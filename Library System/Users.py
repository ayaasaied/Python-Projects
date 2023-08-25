class Users:
    def __init__(self ,name ,age , address ,email) :
        self.name=name
        self.age=age
        self.address=address
        self.email=email
        
    def __str__(self) : 
        return f"Name :{self.name} | age:{self.age} |email {self.email}"   