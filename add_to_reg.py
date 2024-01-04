import os
import winreg as reg

# Replace with the path of your application
app_path = r".\dist"
app_name = "Create New File"

# Context menu entry for files
key_path = r'*\shell\{}'.format(app_name)

try:
    # Open the registry key and create if it doesn't exist
    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
    reg.SetValue(key, '', reg.REG_SZ, app_name)

    # Create command key
    command_key = reg.CreateKey(key, r'command')
    reg.SetValue(command_key, '', reg.REG_SZ, app_path + ' "%1"')  # '%1' is used for file path

    print(f"{app_name} added to context menu.")

except PermissionError:
    print("Permission Denied: You need to run this script as an administrator.")
finally:
    if 'key' in locals():
        reg.CloseKey(key)
    if 'command_key' in locals():
        reg.CloseKey(command_key)
