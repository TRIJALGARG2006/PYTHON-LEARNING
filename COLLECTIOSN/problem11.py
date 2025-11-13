class mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
class father:
    fathername = ""
    def father(self):
        print(self.fathername)
class son(mother,father):
    def parents(self):
        print("father:",self.fathername)
        print("mother:",self.mothername)

s1 = son()
s1.fathername = "john"
s1.mothername = "jane"
s1.parents()

#multi level inheritance
class grandpa:
    def __init__(self,grandpaname):
        self.grandpaname = grandpaname

class father(grandpa):
    def __init__(self,fathername,grandpaname):
        self.fathername = fathername
        grandpa.__init__(self,grandpaname)

class son(father):
    def __init__(self,sonname,fathername,grandpaname):
        self.sonname = sonname
        father.__init__(self,fathername,grandpaname)
    def print_name(self):
        print("son name:",self.sonname)
        print("father name:",self.fathername)
        print("grandpa name:",self.grandpaname)

s1 = son("mike","john","robert")
s1.print_name()

#hierarchical inheritance

class child2(parent):
    def func3(self):
        print("this is function 3 from child2 class")

object1 = child1()
object2 = child2()

object1.func1()
object2.func1()
object1.func2()
object2.func3()




