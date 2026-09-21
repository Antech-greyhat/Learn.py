def add_setting(settings,key_value):
    key,value = key_value
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '[key]' added with value '[value]' successfully!"
    else:
        return f"Setting '[key]' already exists! Cannot add a new setting with this name."

def update_setting(settings,key_value):
    key,value = key_value
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"setting '{key}' update to '{value}' successfully!"
    else:
        return f"setting '{key}' does not exist! cannot update a non-existing setting."


def delete_setting(settings,key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"setting '{key}' deleted successfully!"
    else:
        return f"setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current User Settings:\n"
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"
    return result
test_settings = {}
print(add_setting(test_settings, ('Theme', 'Dark')))
print(add_setting(test_settings, ('Language', 'English')))
print(update_setting(test_settings, ('Theme', 'Light')))
print(view_settings(test_settings))
print(delete_setting(test_settings, 'Language'))
print(view_settings(test_settings))