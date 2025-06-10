from dataclasses import dataclass, field

@dataclass
class Human:
    name: str
    age: int

    # Adding a method to the dataclass

    def greet(self):
        return f" I am {self.name} and I am {self.age} years old."  


    def work(self):
        return f"{self.name} is working."
    
person1  = Human(name="Alice", age=30)  
print(person1)
print(person1.name)
print(person1.age)
print(person1.greet())  # Check if person1 is equal to itself

