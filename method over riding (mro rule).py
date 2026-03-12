#method over writing(method resultion operation)
class grandfather():
    def gl(self):
        print("this is grand:")
class father():
    def f1(self):
        print("this is father class:")
class child(father,grandfather):
    def c1(self):
        print("this is child class:")

c=child()
c.f1()
print(child.__mro__)
print(child.mro())
