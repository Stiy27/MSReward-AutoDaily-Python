from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None
    
#executables = [Executable("MSReward")]

packages = ["idna"]
options = {
    'build.exe': {
        'packages': packages,
    },
}

setup(
    name="MSReward",
    version="0.1",
    description="Executa pesquisas automáticas no MS Rewards",
    options=options,
    executables=[Executable("edge-automatizado.py", base=base)],
)