# Laptop Refresh Rate Changer
## What is this?
It's a simple python script that changes the display refresh rate when the laptop charger is disconnected / connected (Currently the Changer.exe file only changes from 60Hz to 165Hz and vice versa).

## Why?
ASUS made me angry. (They apparently had this functionality built in Armoury Crate but from what I could find, they removed it)

## Usage
I included a task scheduler xml to import, as of right now it wants the Changer.exe to be in following path "C:\Refresh Rate Change\Changer.exe".

To change the path, change the following ``<Command>"C:\Refresh Rate Change\Changer.exe"</Command>``.

## Info
The Changer.exe file is made from the python code, might trigger the windows antivirus, you can choose to use the one i gave or compile your own using either auto-py-to-exe or pyinstaller using a command like the following ``pyinstaller --noconfirm --onefile --windowed --icon "Path/to/folder/change.ico"  "Path/to/folder/Changer.py"``.

## Future Plans
I'll work on making it so you choose the refresh rates to change between the first time the program is run and not having to import the task scheduler xml file.
