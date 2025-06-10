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
    
    # Adding a callable method to the dataclass
    def __call__(self):
        return f"{self.name} is called."
    
person1  = Human(name="Asif", age=30)  
print(person1)
print(person1.name)
print(person1.age)
print(person1.greet()) 
print(person1.work()) 
print(person1()) ## Calling the dataclass instance as a callable

