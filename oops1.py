# initiate a Class
class employee:
    # special method/ magic method/ dunder method - constructor
    def __init__(self):
        #print(id(self))
        #print("Started executing attributes / data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        #print("Attributes / data have been initiated")
        
    def travel(self):
        print("This travel method was called manually")
        print(f"Employee is now travelling to Delhi")      
        
        
# create an obj/instance of the class
sam = employee()
#sam.name = "D4n0nin0"
#print(id(sam))
#print(sam.name)

#shaktiman = employee()
#print(id(shaktiman))

# printing the attributes
#print(sam.salary)

# calling a method   
#sam.travel()  

# print(type(sam))  