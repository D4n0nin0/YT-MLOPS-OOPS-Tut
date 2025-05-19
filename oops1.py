# initiate a Class
class employee:
    # special method/ magic method/ dunder method - constructor
    def __init__(self):
        print("Started executing attributes / data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes / data have been initiated")
        
    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")      
        
        
# create an obj/instance of the class
sam = employee()

# printing the attributes
# print(sam.salary)

# calling a method   
sam.travel("Kerala")    