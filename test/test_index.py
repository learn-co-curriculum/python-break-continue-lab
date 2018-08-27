import pytest
from ipynb.fs.full.index import first_dog_person, iteration_count, cat_owners, thirty_something_yr_old, dog_owner_names, dog_names, cat_owner_names, cat_names, list_of_odd_numbers_plus_ten

def test_find_first_dog_person():
    assert first_dog_person == {'name': "Katie", 'age': 30, 'job': "Teacher", 'pet': "Dog", 'pet_name': "Frank"}
    assert iteration_count > 0
    assert iteration_count <= 2

def test_cat_owners():
    assert type(cat_owners) == type([])
    assert len(cat_owners) == 2
    assert cat_owners == [{'name': 'Owen', 'age': 26, 'job': 'Sales person', 'pet': 'Cat', 'pet_name': 'Cosmo'}, {'name': 'Josh', 'age': 22, 'job': 'Student', 'pet': 'Cat', 'pet_name': 'Chat'}]

def test_thirty_something_yr_old():
    assert type(thirty_something_yr_old) == type({})
    assert thirty_something_yr_old == {'name': "Katie", 'age': 30, 'job': "Teacher", 'pet': "Dog", 'pet_name': "Frank"}

def test_dog_owner_names():
    assert type(dog_owner_names) == type([])
    assert dog_owner_names == ['Katie', 'Estelle', 'Gustav']

def test_dog_names():
    assert type(dog_names) == type([])
    assert dog_names == ['Frank', 'Gabby', 'Helen']

def test_cat_owner_names():
    assert type(cat_owner_names) == type([])
    assert cat_owner_names == ['Daniel', 'Owen', 'Josh']

def test_cat_names():
    assert type(cat_names) == type([])
    assert cat_names == ['Gato', 'Cosmo', 'Chat']

def test_list_of_odd_numbers_plus_ten():
    assert type(list_of_odd_numbers_plus_ten) == type([])
    assert len(list_of_odd_numbers_plus_ten) == 35
    assert list_of_odd_numbers_plus_ten == [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79]
