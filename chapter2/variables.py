# Decare a variable
f = 0
print(f)

# Re-declare variable
f = "abc"
print(f)

# cannot combine different types of variables
print('this is a string ' + str(123))


# Global vs local variables
def someFunction():
    global f
    f = 'def'
    print(f)


someFunction()
print(f)

