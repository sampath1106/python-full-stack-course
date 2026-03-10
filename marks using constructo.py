class marks:
    def __init__(self,marks):
        self.marks=marks
    def val(self):
        if self.marks>550:
            print("free")
        elif self.marks >500 and self.marks<=449:
            print(40000)
        elif self.marks>450 and self.marks<=500:
            print(50000)
        else:
            print(70000)
c=marks(500)
c.val()

        
        
