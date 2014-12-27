class User():
    def __init__(self,name='',pwd='',email=''):
        self.name = name
        self.pwd = pwd
        self.email = email
    def __str__(self):
        return self.name

a = User('1','2','3')
b = User(name='Ajeeb')
c = User(name='Riyz')
print a,b,c
