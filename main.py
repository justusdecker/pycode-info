import os
import math

EXCLUDED_END = ['.exe','.png','.i','.pyc','.zip','.cfg','.pyz','.toc','.pkg','.spec','.ico','.dll']
FORBIDDEN_FOLDERS = ['.git','.vscode','.pytest','build','dist']

LANGS = {}
FILES = {}

LINES = {}

def convert_bytes(size_bytes):
    if size_bytes == 0:
        return "0B"
    base = 1024
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    unit_index = int(math.log(size_bytes, base))
    unit_index = min(unit_index, len(units) - 1)
    converted_size = size_bytes / (base ** unit_index)
    return f"{converted_size:.0f} {units[unit_index]}"

for root, dirs, files in os.walk('./'):
    for file in files:
        if not file.endswith(tuple(EXCLUDED_END)):
            full_path = os.path.join(root, file)
            
            if not any([ff in full_path for ff in FORBIDDEN_FOLDERS]):
                if not file.split('.')[-1] in LANGS:
                    LANGS[file.split('.')[-1]] = os.path.getsize(full_path)
                else:
                    LANGS[file.split('.')[-1]] += os.path.getsize(full_path)
                
                if not file.split('.')[-1] in FILES:
                    FILES[file.split('.')[-1]] = 1
                else:
                    FILES[file.split('.')[-1]] += 1
                
                with open(full_path,'rb') as f:
                    _file = f.read()
                _file = _file.decode().splitlines()
                if not file.split('.')[-1] in LINES:
                    LINES[file.split('.')[-1]] = len(_file)
                else:
                    LINES[file.split('.')[-1]] += len(_file)
                        
total = sum(LANGS.values())
for lang,files in zip(LANGS,FILES):
    print(f'{lang} {LANGS[lang] // 1024} KB in {FILES[files]} files {(LANGS[lang]/total):.2%}')
    

    
    
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[90m']
RESET_COLOR = '\033[0m'

color_index = 0
for lang in LANGS:

    percentage = LANGS[lang] / total

    bar_length = 50
    filled_length = int(bar_length * percentage)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)

    color = COLORS[color_index % len(COLORS)]
    color_index += 1

    print(f'{lang:<10} | {convert_bytes(LANGS[lang]):7}  | {FILES[lang]:4} Files | {color}{bar}{RESET_COLOR} ({percentage:.2%}) - {LINES[lang]} lines')
    
print(f'{sum(FILES.values())} Files')
