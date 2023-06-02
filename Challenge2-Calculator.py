class Calculator:
    def __init__(self, num1,num2):
          self.num1 =num1
          self.num2 = num2
    def  add(self):
         return self.num1+self.num2
    def subtract(self):
         return self.num2-self.num1
    def multiply(self):
         return self.num1*self.num2
    def divide(self):
        return self.num2 / self.num1
obj= Calculator(10,15)
result_add=obj.add()
result_sub=obj.subtract()
result_divide=obj.divide()
result_multiplication=obj.multiply()
print(result_add)
print(result_sub)
print(result_multiplication)
print(result_divide)




    
