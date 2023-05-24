#Inheritance
class Polygon:
    #Initializing the number of sides
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)] #a list comprehension that creates a list of zeros with the length specified by the variable 'no_of_sides'

    def inputSides(self):
        self.sides = [float(input("Enter side " +str(i+1)+ ":")) for i in range(self.n)]  #depending upon the value assigned to self.sides, lets assume 3 so when this code executes
        #it will prompt the user to enter the lengths of three sides and those input values are converted into float. Here loop is from 0 i.e. 0, 1, 2, however when 1 added it becomes 1, 2, 3.
    
    #method to display length of each sides of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])
class Triangle(Polygon):
    #Initializaing the number of sides of a triangle to 3 by calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self, 3) 
    def findArea(self):
        a, b, c = self.sides
        s = (a+b+c)/2 #semi-perimeter of a triangle
        a = (s*(s-a)*(s-b)*(s-c))**0.5 #area of a triangle
        print("The area of a triangle is %0.2f" %a)

x = Triangle()
x.inputSides()
x.dispSides()
x.findArea()
