from cx_Freeze import setup, Executable

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