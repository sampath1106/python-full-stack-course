class father():
    def pl(self):
        print("this is father class:")
class mother(father):
    def d1(self):
        
        print("hii raa:")
class child(mother):
    def c1(self):
        
        print("amma nana:")
p=child()
p.d1()
c=child()
c.c1()
c.d1()
