def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}! ".format(name=name)

name = 'Ryan'
print(greet(name))