'''Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.
'''

guest_list  = ["Kim", "Lee", "Park"]
print(guest_list)

shrinked_guest_list = guest_list.pop()
print(f"Sorry {shrinked_guest_list}, I can't invite you to dinner.")

print(guest_list)

print(f"You both {guest_list[0]} and {guest_list[1]} are  invited to dinner.")

print(guest_list)

del guest_list[0]
del guest_list[0]

print(guest_list)



# Sorting List 

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) #original order
cars.sort() #after sorting
print(cars)
cars.sort(reverse=True) #reverse sorting
print(cars)

cars.reverse()
print(cars) #original order