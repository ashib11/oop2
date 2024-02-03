class Rectangle:
    def __init__(self, width, height):
        self.width = width;
        self.height = height; 
    def display(self):
        print("The area of the triangle is ", self.width*self.height, end="\n");
        print("The perimeter of the reactangle is ", 2*(self.height+self.width))
        
obj1 = Rectangle(10,20);
obj1.display();
print("\n");
obj2 = Rectangle(20,30);
obj2.display();   
