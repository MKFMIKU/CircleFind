from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\meikangfu\\AppData\\Local\\Continuum\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\meikangfu\\AppData\\Local\\Continuum\\Anaconda3\\tcl\\tk8.6"

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [Executable("main.py", base=base)]

packages = ["os"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "CircyeX",
    options = options,
    version = "0.1",
    description = 'By MKF',
    executables = executables
)