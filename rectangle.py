class Rectangle:
   def __init__ (self,a=0,b=0):
       self.a=a
       self.b=b
   def surface(self):
     return self.a*self.b

r1 = Rectangle ();
r2 = Rectangle (5,4);
print("la surface est:",r1.surface())
print("la surface est:",r2.surface());