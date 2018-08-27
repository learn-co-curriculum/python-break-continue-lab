
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
    pass
```


```python
# use a for loop to create a list of the cat owners who are under the age of 28
# remember to use break and continue to make your code more efficient
cat_owners = None
# for loop goes here
```


```python
# use a for loop to find the first person who is above 29 years old in our list of people
# remember to use a break and or continue statement
thirty_something_yr_old = None
# for loop goes here
```


```python
# use a for loop to create a list of person names and another list of pet names for all dog owners
# remember to use break and or continue statements
dog_owner_names = None
dog_names = None
# for loop goes here
```


```python
# use a for loop to create a list of person names and another list of pet names for all cat owners this time
# remember to use break and or continue statements
cat_owner_names = None
cat_names = None
# for loop goes here
```


```python
# use a for loop to create a list of odd numbers from the list of numbers from 0 to 100
# each time there is an odd number, add 10 to it and append it to the list_of_odd_numbers_plus_ten
# stop adding numbers to the list when there are 35 numbers
# use break and continue statements in your code
list_of_numbers = list(range(0,100))
list_of_odd_numbers_plus_ten = []
for number in list_of_numbers:
    pass
```

## Summary

In this lab, we practiced using flow control with `break` and `continue` to selectively operate on elements, append them to new lists, or assign them to new variables.
