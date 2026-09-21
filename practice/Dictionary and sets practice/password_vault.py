def add_account(vault,account_tuple):
    site_name,password = account_tuple
    clean_site_name = site_name.lower()
    if clean_site_name in vault:
        return f"'{clean_site_name}' already exist"
    else:
        vault[clean_site_name] = password
        return f"success account for '{clean_site_name}' has been added"

def update_password(vault,account_tuple):
    name,password = account_tuple
    name = name.lower()
    if name in vault:
        vault[name] = password
        return f"Success the '{password}' has been updated."
    else:
        return f"The '{name}' does not exist."

def remove_account(vault,site_name):
    site_name = site_name.lower()
    if site_name in vault:
        vault.pop(site_name)
        return f"'{site_name}' has been deleted successfully!"
    else:
        return f" '{site_name}' not found!"

def view_account(vault):
    if not vault:
        return 'Error: there are no saved accounts'
    else:
        return f" Saved Accounts: '{vault}'"