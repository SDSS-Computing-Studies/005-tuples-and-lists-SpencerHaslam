#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list
example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
people = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print (people)
name1 = str(input("Enter a word from the list").strip())
name2 = str(input("Enter another word").strip())
ind = people.index(name1)
people.remove(name1)
people.insert(ind, name2)
print(people)
