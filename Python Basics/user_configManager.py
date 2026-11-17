

"""
User Configuration Manager

What I learned today:

1. Dictionary manipulation:
   - Adding key-value pairs.
   - Updating existing values.
   - Removing keys using del.
   - Checking whether a key exists using 'in'.

2. Tuple unpacking:
   - Extracting key and value from a tuple.
   - Example: key, value = pair.

3. String methods:
   - .lower() converts strings to lowercase.
   - .capitalize() capitalizes the first letter.
   - .items() retrieves dictionary keys and values.

4. Conditional logic:
   - Using if/else to handle existing and missing keys.
   - Returning different messages depending on conditions.

5. String formatting:
   - Using f-strings to dynamically insert variables.
   - Using \n to format output across multiple lines.

6. Functions:
   - Passing dictionaries and tuples as arguments.
   - Modifying dictionaries directly inside functions.
   - Using return to send results back to the caller.

Project objective:
Build a configuration manager that allows users to
add, update, delete, and view their preferences.
"""

test_settings = {
    'theme': 'light',
    'language': 'english',
    'notifications': 'enabled'
}

def add_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current User Settings:\n"

    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result
# Testing the functions
print(view_settings(test_settings))

print(add_setting(test_settings, ('volume', 'high')))
print(update_setting(test_settings, ('theme', 'dark')))
print(delete_setting(test_settings, 'language'))

print("\nUpdated settings:")
print(view_settings(test_settings))