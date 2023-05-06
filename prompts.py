# Please complete the following functions.

# name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.

def name_args(**kwargs):
    for k in kwargs.keys():
        print(f'{k}:{kwargs[k]}')
name_args(name = 'james', age = 23)
# all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.

def all_true(elemt):
    return all(elemt)

print( all_true([True, True, True]))
print( all_true([True, True, False]))

