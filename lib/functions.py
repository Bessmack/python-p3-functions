#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    summation = num1+num2
    print(summation)
    return summation

def halve(number):
    divided = number/2
    print(divided)
    return divided

greet_programmer()
greet('Steve')
greet_with_default('Brenda')
add(10,75)
halve(46)