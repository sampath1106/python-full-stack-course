class codegnan:
    institute="reddy"
    
    def __init__(self,name,marks,college,course):
        self.name=name
        self.marks=marks
        self.college=college
        self.course=course
    def details(self):
        print(self.name,self.marks,self.college,self.course)
    
c=codegnan("ajay",100,"dd","oops")
c.details()
