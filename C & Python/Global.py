

name = "Global Monica"  # Global Scope

def outer():
    name = "Enclosing Monica"  # Enclosing Scope

    def inner():
        name = "Local Monica"  # Local Scope
        print(name)

    inner()

outer()