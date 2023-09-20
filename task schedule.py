import os

command = 'schtasks /create /tn "Change Refresh Rate" /sc ONEVENT /ec Microsoft-Windows-Kernel-Power /mo "*[System[Provider[@Name=\'Microsoft-Windows-Kernel-Power\'] and EventID=105]]" /rl HIGHEST /tr "C:\\Refresh Rate Change\\Changer.exe" /f'

os.system(command)

