#hetrarical inhertance
class father():
     def f1(self):
         
         print("this  is father:")
class child1(father):
         def c1(self):
             print("this is child one:")
class child2(father):
        def c2(self):
            
             print("this is child two:")
c2=child1()
c2.c1()
c2.f1()
