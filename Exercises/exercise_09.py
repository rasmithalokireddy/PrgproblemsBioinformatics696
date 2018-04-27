"""
Exercise 9


1) Write a decorator function that prints the:
     - real world time taken to run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowlege of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math


def time_decorator(my_def):
    def internal_wrapper():
        t0 = time.time()
        tp1=time.process_time()
        def_result = my_def()
        t1 = time.time()
        tp2=time.process_time()
        print("'{}' finished in real world time in {} seconds".format(my_def.__name__, t1-t0))
        print("'{}' finished in process time in {} seconds".format(my_def.__name__, tp2 - tp1))
        print("'{}' size of the return value {} ".format(my_def.__name__, sys.getsizeof(def_result)))
        return def_result
    return internal_wrapper # remember, 'internal_wrapper' is not the same as 'internal_wrapper()'




# print(time_decorator(for_loop))

@time_decorator

def for_loop():
    my_list= []
    for x in range(1,1000001):
        my_list.append(x)
    return my_list

time_decorator(for_loop())

@time_decorator

def list_comp():

    list=[i for i in range(1,1000001)]
    return list

time_decorator(list_comp())

@time_decorator
def numpy_list():
    return numpy.arange(1,1000001)

time_decorator(numpy_list())

@time_decorator
def pandas_list():

   return pandas.DataFrame(numpy.arange(1,1000001))

time_decorator(pandas_list())
@time_decorator
def generator_list():

    return (i for i in range(1, 1000001))

time_decorator(generator_list())

@time_decorator
def for_loop_log():
    my_list = []
    for x in range(1, 1000001):
        my_list.append(math.log(x))
    return my_list

time_decorator(for_loop_log())

@time_decorator
def list_com_log():
    return [math.log(i) for i in range(1, 1000001)]

time_decorator(list_com_log())

@time_decorator
def numpy_list_log():
    return numpy.log10(numpy_list())

time_decorator(numpy_list_log())

@time_decorator
def pandas_list_log():
    return pandas.DataFrame(numpy.log10(numpy_list()))
time_decorator(pandas_list_log())

@time_decorator
def generator_list_log():
    return (math.log(i) for i in range(1, 1000001))

time_decorator(generator_list_log())





