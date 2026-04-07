class Cat():
    def __init__(self,name,breed,age):

        self.name=name
        self.breed=breed
        self.age=age
    def information(self):
        return {"Ім'я" : self.name,
                "Порода" :self.breed,
                "вік" : self.age}
obj1=Cat("буся","британський","3")
obj2=Cat("Вася","британський","3")
print(obj1.information())
print(obj2.information())

