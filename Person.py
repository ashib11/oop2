class Person:
    def __init__(self, name, age):
        self.name=name; 
        self.age=age
    def display(self):
        print(self.name,"is", self.age, "years old"); 
person = Person("Ashib", 21); 
person2 = Person("Shuvro", 11);

person.display();
person2.display(); 
print("\nSet new age and name:\n");
person = Person("Ashibur Rahman", 21); 
person2 = Person("Shuvro Rahman", 23);
person.display();
person2.display(); 
