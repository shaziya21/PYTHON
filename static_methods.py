class student:

     school = "telusko"


     def __init__(self,m1,m2,m3):
         self.m1 = m1
         self.m2 = m2
         self.m3 = m3

     def avg(self):
        return(self.m1 + self.m2 + self.m3)/3

     @staticmethod
     def info():
         print('this is a student class.. in abc mmodule')


s1 = student(12,43,76)
s2 = student(32,54,15)


print(s1.avg())
student.info()
