from pathlib import Path

path = Path()
for pri in path.glob('*'):  #  '*.py
    print(pri)