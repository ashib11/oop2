class DIUemployee:
    def __init__(self, name, jobtittle, salary):
        self.name=name; 
        self.jobtittle=jobtittle;
        self.salary=salary; 
    def increment(self, value):
        self.value = value;
        self.salary = self.salary + self.salary*value/100;  
    def display(self):
        print(f"Name: {self.name}\nJob Tittle: {self.jobtittle}\nSalary: {self.salary}" ); 
    def displayafterInterest(self, value):
        print(f"{value}% for '{self.name}':\n"); 
obj1 = DIUemployee("Ashibur", "Manager", 2000);
obj2 = DIUemployee("Shuvro", "Lecturer", 1000); 
print("**********DIU Salary Management System********\n\nEmployee Details:\n");
obj1.display()
print('\n')
obj2.display()
print("\n\nAfter raising salary:\n");
obj1.displayafterInterest(8); 
obj1.increment(8); 
obj1.display();
print('\n');
obj2.increment(10);
obj2.displayafterInterest(10);
obj2.display();  

