import winreg

key_path = r'SOFTWARE\Refresh'
value_name = 'RefreshRate'
value_data = '60, 165'

try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
    try:
        existing_value, _ = winreg.QueryValueEx(key, value_name)
        value_list = [int(x) for x in existing_value.split(',')]
        print(value_list)

        winreg.CloseKey(key)
    except FileNotFoundError:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
        winreg.CloseKey(key)
except Exception as e:
    print(f"Error creating or updating registry key: {str(e)}")
