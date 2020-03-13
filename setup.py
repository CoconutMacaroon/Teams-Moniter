from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Teams_LED_Moniter",
    options = options,
    version = "1.0",
    description = 'A Microsoft Teams moniter',
    executables = executables
)