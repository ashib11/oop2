class Library:
    def __init__(self, authorName, bookTittle, edition,bookNo):
        self.authorName = authorName; 
        self.bookTittle = bookTittle; 
        self.edition = edition;
        self.bookNo = bookNo;
    def display(self):
        print("Book", self.bookNo, ":", self.bookTittle , ", Author:", self.authorName, ", Edition: " + self.edition); 
book1 = Library("Pk Sinha", "Introduction to Computer Fundamental", "5th", 1); 
book2 = Library("Thomas H.", "Introduction to Algorithm", "6th", 2);

print("*******Digital Library of DIU: Book list*****", end="\n\n"); 
book1.display(); 
book2.display(); 

print("\n\nInformation Updated!!\n\nUPDATED INFORMATION:\n\n")

book1 = Library("Pk Sinha", "Introduction to Computer Fundamental", "6th", 1); 
book2 = Library("Thomas H. Cormen, Charles Leiserson, ronald L, Rivest and Clifford Stein", "Introduction to Algorithm", "6th", 2);

book1.display();
book2.display(); 
