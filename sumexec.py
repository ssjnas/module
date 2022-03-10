import mymodule
from Mymodule1 import Student
from Mymodule2 import Cart
import datetime 
print("sum:",  mymodule.sum_of_series(10))
print("square:",  mymodule.square(25))
print( "cube:",  mymodule.s(25))
print(mymodule.myFunction("hello","Howareyou","Fine"))
print(mymodule.validPassword("pras123"))
s1=Student("ram",20,30,"CVR")
s1.talk()
s1=Student("Rahim",40,35,"VNR")
s1.talk()
date_object = datetime.date.today()
print(date_object)
a=Cart()
a.add_item("Dairymilk", 10)
print(a.display_items())
