import ctypes
import ctypes.wintypes

# Constants for the ChangeDisplaySettingsEx function
CDS_UPDATEREGISTRY = 0x01
CDS_GLOBAL = 0x08
DISP_CHANGE_SUCCESSFUL = 0
ENUM_CURRENT_SETTINGS = -1

# Define the DEVMODE structure
class DEVMODE(ctypes.Structure):
    _fields_ = [
        ("dmDeviceName", ctypes.wintypes.WCHAR * 32),
        ("dmSpecVersion", ctypes.wintypes.WORD),
        ("dmDriverVersion", ctypes.wintypes.WORD),
        ("dmSize", ctypes.wintypes.WORD),
        ("dmDriverExtra", ctypes.wintypes.WORD),
        ("dmFields", ctypes.wintypes.DWORD),
        ("dmPositionX", ctypes.wintypes.LONG),
        ("dmPositionY", ctypes.wintypes.LONG),
        ("dmDisplayOrientation", ctypes.wintypes.DWORD),
        ("dmDisplayFixedOutput", ctypes.wintypes.DWORD),
        ("dmColor", ctypes.wintypes.SHORT),
        ("dmDuplex", ctypes.wintypes.SHORT),
        ("dmYResolution", ctypes.wintypes.SHORT),
        ("dmTTOption", ctypes.wintypes.SHORT),
        ("dmCollate", ctypes.wintypes.SHORT),
        ("dmFormName", ctypes.wintypes.WCHAR * 32),
        ("dmLogPixels", ctypes.wintypes.WORD),
        ("dmBitsPerPel", ctypes.wintypes.DWORD),
        ("dmPelsWidth", ctypes.wintypes.DWORD),
        ("dmPelsHeight", ctypes.wintypes.DWORD),
        ("dmDisplayFlags", ctypes.wintypes.DWORD),
        ("dmDisplayFrequency", ctypes.wintypes.DWORD),
        ("dmICMMethod", ctypes.wintypes.DWORD),
        ("dmICMIntent", ctypes.wintypes.DWORD),
        ("dmMediaType", ctypes.wintypes.DWORD),
        ("dmDitherType", ctypes.wintypes.DWORD),
        ("dmReserved1", ctypes.wintypes.DWORD),
        ("dmReserved2", ctypes.wintypes.DWORD),
        ("dmPanningWidth", ctypes.wintypes.DWORD),
        ("dmPanningHeight", ctypes.wintypes.DWORD),
    ]

def main():
    # Initialize DEVMODE structure
    dm = DEVMODE()
    dm.dmSize = ctypes.sizeof(DEVMODE)

    # Get the current display settings
    if ctypes.windll.user32.EnumDisplaySettingsW(None, ENUM_CURRENT_SETTINGS, ctypes.byref(dm)):
        # Set the desired display frequency (e.g., 165)
        dm.dmDisplayFrequency = 165

        # Change the display settings
        result = ctypes.windll.user32.ChangeDisplaySettingsExW(None, ctypes.byref(dm), None, CDS_UPDATEREGISTRY | CDS_GLOBAL, None)

        # Check the result
        if result == DISP_CHANGE_SUCCESSFUL:
            print("Display settings changed successfully.")
        elif result == 4:
            print("The computer must be restarted for the graphics mode to work.")
        else:
            print("Display settings change was unsuccessful. Error code:", result)

if __name__ == "__main__":
    main()
