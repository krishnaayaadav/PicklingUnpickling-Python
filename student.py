class Student:
    """This is Student Class attributes are:name:str age:int and email:str only"""

    def __init__(self, name:str, age:int, email:str):
        self.name = name
        self.age  = age
        self.email = email

    
    def detail(self):
        print('\nStudent Details are: ')
        print(f'Name: {self.name} Age: {self.age} Email: {self.email}')
