class Course:
    def __init__(self, name, instructor, duration):
        self.name = name
        self.instructor = instructor
        self.duration = duration

    def display_info(self):
        print(f"Course: {self.name}")
        print(f"Instructor: {self.instructor}")
        print(f"Duration: {self.duration} weeks")

    def enroll(self, student):
        print(f"\n{student} has enrolled in {self.name} course led by {self.instructor} for {self.duration} weeks.")

class Cat: 
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def display_info(self):
        print(f"Cat's name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")

    def meow(self):
        print(f"\n{self.name} is a cute {self.age} year old {self.breed} cat that says 'meow' all night long.")

class Shoes:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color

    def display_info(self):
        print(f"Shoes brand: {self.brand}")
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")

    def wear(self):
        print(f"\nI am wearing a {self.color} {self.brand} shoes in size {self.size} to look cool.")

# Creating objects for each class
course1 = Course("Data Structures", "Sir Jayvee", 15) #instance of the course class 
cat1 = Cat("Ginger", "Persian", 5)
shoes1 = Shoes("Adidas", "7", "Black")

# Printing properties and running methods for each object
print("\nCourse Info: \n")
course1.display_info()
course1.enroll("JHESCKIE")

print("\nCat Info: \n")
cat1.display_info()
cat1.meow()

print("\nShoes Info: \n")
shoes1.display_info()
shoes1.wear()
