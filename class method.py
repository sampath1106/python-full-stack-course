class method:   # one class method using given input in program
        
    def find_val(self,val):
        
        self.val=val
        if(self.val)%2==0:
            print("even:")
        else:
            print("odd:")
d1=method()
d1.find_val(40)



class method:   #  to give output manually at output 
        
    def find_val(self):
        
        self.val=int(input("enter a number:"))
        if(self.val)%2==0:
            print("even:")
        else:
            print("odd:")
d1=method()
d1.find_val()
