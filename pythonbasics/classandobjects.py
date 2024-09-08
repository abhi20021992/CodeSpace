class FirstClass :
    def __init__(self) -> None:
        self.name =  'abhishek'
    
    def printfn(self): #class instance is passed in as first variable of the function need not to be passed 
        #its resambles like this in js
        print(self.name)

FirstClass().printfn()

obj = FirstClass() #obj contain a instance of our class


# self is special keyword exactly like this in js
# __init__ is constructor of the class and has access to self
# be carefull about the instance variable and class variable 
class MyClass:
    _data = 10
    def __init__(self, x) -> None:
        self._data = x
        
    #this is instance method as this contain self as one param, now when we create instance of this class we can access it with
    #instance variable
    def customMethod(self, data):
        print(data)
        
    #this is static method cant be accessed by instance of the class, always need to call this by class name
    def statiMehod(data):
        print(data)
    
     #this is static method can be accessed by instance of the class, always need to call this by class name
    @staticmethod
    def decoratedStaticMethod(data):
        print(data)
    
myInstance = MyClass(9)
print(myInstance._data)# instance variable value is changed to 9
print(MyClass._data)# will result in 10 as this is class or static variable and this value is not changed due to instace value 

#myInstance.statiMehod('static method')# lead to an error
# how ever in case of static and instance variable we can use instance and class name interchangably as showdn above
myInstance.decoratedStaticMethod('decorated method')
myInstance.customMethod('instance method')
MyClass.statiMehod('Class method or static method')

#in order to hande this confucsion we use a decorator @staticmethod above the class static method and then we can use self variable


#extending syntax for a class is using like function 

class Parent:
    pass

class Child(Parent):
    pass

#we can override methods from parent in child and then calling of function will depend on instance on which it is called
# to access parent methods in child class we need to use super() function 
# also we should call super().__init__() inside the construction (__init__) of the child class so that it will create instance 
#of the parent first