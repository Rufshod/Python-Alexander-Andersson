import os, sys

def newline():
    return print("\n")

os.system("cls||clear") # Clears the terminal when it runs.

print(f"{'='*30}main.py{'='*30}")

#Code imported from another module is executed when imported.
import module1

# note __name__ is module1 when ran from outside of module1.py
# when module1.py is ran -> __name__ = "__main__"
# when we run it here __name__ = "module1"

newline()
#when importing a module - a reference will be created to sys.modules
print("globals namespace")

print(globals()["module1"])
newline()
# when importing a module - iit will be stored in sys.modules
print("sys.modules")

print(sys.modules["module1"])
newline()

print(f"{'='*30}main.py{'='*30}")



#namespace, its where your variables live, global namespace