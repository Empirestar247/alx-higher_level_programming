#!/usr/bin/python3

import importlib.util
import urllib.request

# Specify the URL of the hidden_4.pyc file
url = "https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc"

# Download the hidden_4.pyc file
urllib.request.urlretrieve(url, "hidden_4.pyc")

# Load the compiled module using importlib.util
spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Get all the names defined in the module
names = dir(module)

# Filter out names that start with "__"
filtered_names = [name for name in names if not name.startswith("__")]

# Sort the names alphabetically
filtered_names.sort()

# Print the names
for name in filtered_names:
    print(name)
