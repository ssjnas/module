class Student:
    def __init__(self,name,rollno,marks,college):
        self.name=name
        self.rollno=rollno
        self.marks=marks
        self.college=college
    def talk(self):
        print("Hello My Name is:",self.name) 
        print("My Rollno is:",self.rollno) 
        print("My Marks are:",self.marks)
        print("My college is:{}".format(self.college))
    def details(self):
        print("My company name is:",self.name)
        print("my job Location:",self.location)
        print("mobile Number:",self.number)
        
s1=Student("prashanth reddy","14241A0320",79,"GRIET") 
s1.talk()
