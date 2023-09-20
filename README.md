# Display Refresh Rate Changer
Changing the display refresh rate when the laptop charger is disconnected (Currently the Changer.exe file only changes between 60Hz and 165Hz)

I included a task scheduler xml to import, as of right now it wants the Changer.exe to be in following path "C:\Refresh Rate Change\Changer.exe"
To change the path, change the following ``<Command>"C:\Refresh Rate Change\Changer.exe"</Command>``

I'll work on making it so you choose the refresh rates to change between and not having to import the task scheduler xml file.
