
class Manager:
    def __init__(self, name, age,motherLanguage):
        self.name=name
        self.age=age
        self.language={motherLanguage}
    def addLanguage(self,language):
        self.language.add(language)


class Employees:
    def __init__(self, name, age,motherLanguage):
        self.name=name
        self.age=age
        self.language={motherLanguage}
    def addLanguage(self,language):
        self.language.add(language)
employee1=Employees("Jack",22,"English")
employee2=Employees("Mahmut",26,"Turkish")
employee1.addLanguage("German")
employee2.addLanguage("French")
print(employee1.name," = " ,employee1.language)
print(employee2.name," = " ,employee2.language)
manager1=Manager("Steve",36,"Arabish")
manager2=Manager("Hasan",25,"Arabish")
manager1.addLanguage("Russian")
manager2.addLanguage("Spanish")
print(manager1.name," = " ,manager1.language)
print(manager2.name," = " ,manager2.language)

   