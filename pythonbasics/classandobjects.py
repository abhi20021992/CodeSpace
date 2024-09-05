class FirstClass :
    def __init__(self) -> None:
        self.name =  'abhishek'
    
    def printfn(self): #class instance is passed in as first variable of the function need not to be passed 
        #its resambles like this in js
        print(self.name)

FirstClass().printfn()

obj = FirstClass() #obj contain a instance of our class
