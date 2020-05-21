import os
import inspect

this_file = inspect.getfile(inspect.currentframe())
dirpath = os.path.abspath(os.path.dirname(this_file))

print(dirpath)