class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):

        s = 0

        if a!=None and b!=None and c!=None:
          s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a

        return s


s1 = Student(58,69)
print(s1.sum(5+4+6))
print(s1.sum(5+4))
print(s1.sum(5))


                        (---Method Overriding---)

class A:

    def show(self):
        print("in A Show")

class B(A):

    def show(self):
        print("in B Show")


a1 = B()
a1.show()
