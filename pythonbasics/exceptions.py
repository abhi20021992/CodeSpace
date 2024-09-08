try:
    1/0
except Exception as e:
    print(type(e))
finally:
    print('finally run')
    
    
#exceptions are of type class and they all extend Exception and then base exception class

try:
    1/0
except Exception as e:
    print(type(e))
finally:
    print('finally run')
    
#finally will run even after exception, the finally block will run first and then exception is printed or thrown
# we can also catch exception by their class like ZeroDivisionError, TypeError etc classes
# one point to note is the order of exception block matters as python start checking from top and then stops if match 
#excetption is found

#creating custom decorators to handle exception as shwon below 

def handleException(func):
    def wraperx():
        try:
            func()
        except ZeroDivisionError:
            print('Deviding by zero')
        except TypeError:
            print('Type error happen')
        except Exception:
            print('Unknown exception happend')
        finally:
            print('finally run')
    return wraperx

@handleException
def causeError():
    1/0
    
causeError()

#we see above how to create a annotation, just we need to create a funciton and we need to create a inner function and return it,
#point to note here is the func execution is required as this is the funciton which caused the error
# also we need to put the decoration on top of the function suspect to throw the error.

#now raising an exception is done raise keyword followed by the exception class like TypeError etc

@handleException
def raiseExeption():
    raise TypeError()
    print('exception is throwm')

raiseExeption()

# here we can see ide is saying the print at line 54 will never run , becouse when an exception is thrown the 
# programe halts and return to exepction handler to handle it


#custom exception is mostly used at application level to handle all the possible exception in applicaiton

class CustomException (Exception):
    pass

# above example of custom exception class

def causeError1():
    raise CustomException('my custom exception')

causeError1()

#we can write a full clss with status codes or some keys on which exceptions are categorized also we can add custon messages



    

    