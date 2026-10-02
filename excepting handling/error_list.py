#value error
# try:
#     num = int("abs")
#     print(num)
# except ValueError:
#     print("Invalid value")

#type error
# try:
#     print("10" + 20)
# except TypeError:
#     print("Different data types")

#index error
# try:
#     l = [10, 20, 30]
#     print(l[5])
# except IndexError:
#     print("Index out of range")

#key error
# try:
#     d = {"a": 10}
#     print(d["b"])
# except KeyError:
#     print("Key not found")

#attribute error
# try:
#     num = 10
#     num.append(20)   
#     print(num)
# except AttributeError:
#     print("Attribute does not exist")

#overflow error
# import math
# try:
#     print(math.exp(1000))
# except OverflowError:
#     print("Overflow Error")

#keyboardinterrupt
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     print("keyboard interrupt(ctrl+c)")

#syntaxerror
# if True
#     print("hello")

#assertionerror
# try:
#     age = 14
#     assert age >= 18
# except AssertionError:
#     print("Age must be 18 or above")

#`StopIteration`                  |
# numbers = iter([1, 2, 3])
# try:
#     while True:
#         print(next(numbers))
# except StopIteration:
#     print("No more elements in the iterator.")

#EOF error
# try:
#     name = input("Enter your name: ")
#     print(name)
# except EOFError:
#     print("No input provided.")

#importerror
# try:
#     from math import xyz
# except ImportError:
#     print("cannot import math 'xyz'")

#ModuleNotFoundError
# try:
#     import xyz
# except ModuleNotFoundError:
#     print("no module found 'xyz'")

#recursion error
# try:
#     def test():
#         test()

#     test()
# except RecursionError:
#     print("Recursion limit exceeded.")

#connection  error
# try:
#     raise ConnectionError("unable to connect to server")
# except ConnectionError:
#     print("check your internet connection")

#

