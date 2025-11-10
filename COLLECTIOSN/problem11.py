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