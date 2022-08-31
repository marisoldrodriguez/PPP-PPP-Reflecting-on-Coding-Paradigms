# Functional Prompts
"""
Implement a function that will flatten and sort an array of integers in ascending order.
"""
def flatten_sort(array):
  # assigning an empty list
  array = []
  for item in array:
    for i in item:
      array.append(i)
# sorted is a builtin that returns a new list containing all items from the iterable in ascending order.
  return sorted(array)
print(sorted([3,5,7,4,9,1]))

"""
1)How does this solution ensure data immutability?
By assigning the array's initial value within the method(function), we ensure immutability. Once the function is invoked with an array as its parameter, Python will store this new object in a unique object’s address in memory.

2)Is this solution a pure function? Why or why not?
Yes,it's a pure function because as you provide the same input, the function will always return the same output. This funciton will not produce side effects.

3)Is this solution a higher order function? Why or why not?
No, it is not a higher order function because it does not accept one or more functions as an argument, nor does it return a function.

4)Would it have been easier to solve this problem using a different programming style?
I don't believe so. This programming style is clean, efficient and dry. The use of the builtin method "sorted" allows arranging the iterable in ascending order. 

5)Why in particular is functional programming a helpful paradigm when solving this problem?
It is a declarative type of programming style. Its main focus is on “what to solve” in contrast to an imperative style where the main focus is “how to solve”, as I mentioned the use of the "sorted" method in previous question. Therefore, helps us to solve problems effectively in a simpler way.
"""

# Object Oriented Prompt
"""
Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.
"""
# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

# Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"

# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def boost(self):
    self.max_speed *=2

# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
    
  def flame_jet(self, other):
    other.condition = "trashed"

pod = Podracer(100, "repaired", 300)
pod.repair()
print(pod.condition)

new_pod = AnakinsPod(2, "repaired", 500)
new_pod.boost()
print(new_pod.max_speed)

third_pod = SebulbasPod(5, "thrashed", 150)
third_pod.flame_jet
print(third_pod.condition)

"""
Once an Object Oriented solution has been implemented, answer the following questions:
1)How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
Encapsulation
Abstraction
Inheritance
Polymorphism
answer:
The first pillar that stands out to me is Inheritance. Both the classes AnakinsPod and SebulbasPod inherit from the parent class of Podracer by setting its parameter to Podracer. By using the super() method, we inherit Podracer's attributes and methods when instantiate the class AnakinsPod or SebulbasPod to create an instance of those classes.
Encapsulation is used when constructing a class that has both attributes and methods.
Abstraction is demonstrated in the flame_jet() function. Abstract class of Podracer may not be instantiated, but its abstract methods was implemented by its subclass SebulbasPod.

2)Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
No, OOP makes code more reusable and makes it easier to work with larger programs. 

3)How in particular did Object Oriented Programming assist in the solving of this problem?
OOP programs prevent you from repeating code because a class can be defined once and reused many times.
"""