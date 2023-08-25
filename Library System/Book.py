
class Book:
    #intialize -constructor
    def __init__(self ,title :str ,author :str,descraption :str) :
        self.title=title
        self.descraption=descraption
        self.author=author
     #return object as string format .
    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} |Descreption: {self.descraption}"
        
        
        

