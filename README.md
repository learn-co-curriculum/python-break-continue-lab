
# Break and Continue Statements Lab

## Introduction
In this lab, we will practice using `break` and `continue` statements in our code. We will be iterating through collections and filtering out or selectively operating on elements by using these flow control statements.

## Objectives

* Understand how to use `break` and `continue` statements
* Identify when and where to use `break` and `continue` statements

## Instructions

We have a list of person objects with all kinds of attributes. We'll use loops to find a person that meets a certain requirement that we are looking for or create new lists with a certain subset of elements. Write for loops with conditional statements in conjunction with `break` and `continue` to get the desired output.


```python
people = [
    {'name': "Daniel", 'age': 29, 'job': "Engineer", 'pet': "Cat", 'pet_name': "Gato"}, 
    {'name': "Katie", 'age': 30, 'job': "Teacher", 'pet': "Dog", 'pet_name': "Frank"},
    {'name': "Owen", 'age': 26, 'job': "Sales person", 'pet': "Cat", 'pet_name': "Cosmo"},
    {'name': "Josh", 'age': 22, 'job': "Student", 'pet': "Cat", 'pet_name': "Chat"},
    {'name': "Estelle", 'age': 35, 'job': "French Diplomat", 'pet': "Dog", 'pet_name': "Gabby"},
    {'name': "Gustav", 'age': 24, 'job': "Brewer", 'pet': "Dog", 'pet_name': "Helen"}
]
```


```python
# use the for loop below to find the *first* person in the list of people that has a dog as their pet
# the iteration count shouldn't exceed 2 iterations
first_dog_person = None
iteration_count = 0
for person in people:
    iteration_count += 1
    if person['pet'] == "Dog":
        first_dog_person = person
        break

print(first_dog_person, iteration_count)
```

    {'name': 'Katie', 'age': 30, 'job': 'Teacher', 'pet': 'Dog', 'pet_name': 'Frank'} 2



```python
# use a for loop to create a list of the cat owners who are under the age of 28
# remember to use break and continue to make your code more efficient
cat_owners = []
for person in people:
    if not person['pet'] == "Cat":
        continue
    elif not person['age'] <= 28:
        continue
    else:
        cat_owners.append(person)
        
print(cat_owners)
```

    [{'name': 'Owen', 'age': 26, 'job': 'Sales person', 'pet': 'Cat', 'pet_name': 'Cosmo'}, {'name': 'Josh', 'age': 22, 'job': 'Student', 'pet': 'Cat', 'pet_name': 'Chat'}]



```python
# use a for loop to find the first person who is above 29 years old in our list of people
# remember to use a break and or continue statement
thirty_something_yr_old = None
for person in people:
    if person['age'] >= 30:
        thirty_something_yr_old = person
        break
thirty_something_yr_old
```




    {'name': 'Katie',
     'age': 30,
     'job': 'Teacher',
     'pet': 'Dog',
     'pet_name': 'Frank'}




```python
# use a for loop to create a list of person names and another list of pet names for all dog owners
# remember to use break and or continue statements
dog_owner_names = []
dog_names = []
for person in people:
    if not person['pet'] == "Dog":
        continue
    else:
        dog_owner_names.append(person['name'])        
        dog_names.append(person['pet_name'])
print(dog_owner_names, dog_names)
```

    ['Katie', 'Estelle', 'Gustav'] ['Frank', 'Gabby', 'Helen']



```python
# use a for loop to create a list of person names and another list of pet names for all cat owners this time
# remember to use break and or continue statements
cat_owner_names = []
cat_names = []
for person in people:
    if not person['pet'] == "Cat":
        continue
    else:
        cat_owner_names.append(person['name'])        
        cat_names.append(person['pet_name'])
print(cat_owner_names, cat_names)
```

    ['Daniel', 'Owen', 'Josh'] ['Gato', 'Cosmo', 'Chat']



```python
# use a for loop to create a list of odd numbers from the list of numbers from 0 to 100
# each time there is an odd number, add 10 to it and append it to the list_of_odd_numbers_plus_ten
# stop adding numbers to the list when there are 35 numbers
# use break and continue statements in your code
list_of_numbers = list(range(0,100))
list_of_odd_numbers_plus_ten = []
for number in list_of_numbers:
    if number % 2 == 0:
        continue
    elif len(list_of_odd_numbers_plus_ten) > 34:
        break
    else:
        list_of_odd_numbers_plus_ten.appen
    
        
```

## Summary

In this lab, we practiced using flow control with `break` and `continue` to selectively operate on elements, append them to new lists, or assign them to new variables.
