"""

Functions which take lists as arguments and change them during execution are 
called modifiers and the changes they make are called side effects.A pure 
function does not produce side effects. It communicates with the calling 
program only through parameters, which it does not modify, and a return value. 
Here is double_stuff written as a pure function:

"""


def double_stuff(a_list):
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

mylist = [2, 4, 6]
print(double_stuff(mylist))

"""

Which style is better?

Anything that can be done with modifiers can also be done with pure functions. 
In fact, some programming languages only allow pure functions. There is some 
evidence that programs that use pure functions are faster to develop and less 
error-prone than programs that use modifiers. Nevertheless, modifiers are 
convenient at times, and in some cases, functional programs are less efficient.

In general, we recommend that you write pure functions whenever it is 
reasonable to do so and resort to modifiers only if there is a compelling 
advantage. This approach might be called a functional programming style.

"""