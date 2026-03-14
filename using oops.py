class phone:
    def __init__(self):
        self.contacts={}
    def add(self,name,phone):
        if name not in self.contacts:
            self.contacts[name]=phone
            print("added")
        else:
            print("already")
p1=phone()
p1.add("ajay",1235)
p1.add("ajay",56789)
