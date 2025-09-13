import os
import math
from src.colors import RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, GRAY, RESET_COLOR
FORBIDDEN_FOLDERS = ['.git','.vscode','.pytest','build','dist']

BAR_LENGTH = 50

LANGS = {}
FILES = {}

LINES = {}

LANGUAGE_MAPPER = {
    'Python': ['py'],
    'JavaScript': ['js', 'jsx', 'mjs'],
    'TypeScript': ['ts', 'tsx'],
    'Java': ['java'],
    'C++': ['cpp', 'cc', 'cxx', 'hpp', 'hh', 'hxx'],
    'C': ['c', 'h'],
    'C#': ['cs'],
    'Ruby': ['rb'],
    'Go': ['go'],
    'PHP': ['php'],
    'Swift': ['swift'],
    'Kotlin': ['kt', 'kts'],
    'Rust': ['rs'],
    'HTML': ['html', 'htm'],
    'CSS': ['css'],
    'Shell': ['sh', 'bash', 'zsh', 'bat', 'cmd'],
    'Perl': ['pl', 'pm'],
    'Lua': ['lua'],
    'R': ['r'],
    'Dart': ['dart'],
    'Haskell': ['hs'],
    'Objective-C': ['m', 'mm'],
    'Scala': ['scala'],
    'Elixir': ['ex', 'exs'],
    'Clojure': ['clj', 'cljs', 'cljc'],
    'Erlang': ['erl', 'hrl'],
    'F#': ['fs', 'fsi', 'fsx'],
    'Groovy': ['groovy', 'gvy', 'gy', 'gsh'],
    'Visual Basic': ['vb', 'vbs', 'vbscript'],
    'MATLAB': ['m'],
    'Julia': ['jl'],
    'Tcl': ['tcl', 'tk'],
    'Markdown': ['md'],
    'YAML': ['yaml', 'yml'],
    'JSON': ['json'],
    'XML': ['xml'],
    'Makefile': ['mk', 'makefile'],
    'Dockerfile': ['dockerfile'],
    'Terraform': ['tf'],
    'LICENSE': ['LICENSE'],
}

LANGUAGE_COLOR = {
    'Python': '#3572A5',
    'JavaScript': '#F1E05A',
    'TypeScript': '#2B7489',
    'Java': '#B07219',
    'C++': '#F34B7D',
    'C': '#555555',
    'C#': '#178600',
    'Ruby': '#701516',
    'Go': '#00ADD8',
    'PHP': '#4F5D95',
    'Swift': '#FFAC45',
    'Kotlin': '#F18E33',
    'Rust': '#DEA584',
    'HTML': '#E34C26',
    'CSS': '#563D7C',
    'Shell': '#89E051',
    'Perl': '#0298C3',
    'Lua': '#000080',
    'R': '#198CE7',
    'Dart': '#00B4AB',
    'Haskell': '#5E5086',
    'Objective-C': '#438EFF',
    'Scala': '#C22D40',
    'Elixir': '#6E4A7E',
    'Clojure': '#DB5855',
    'Erlang': '#B83998',
    'F#': '#B845FC',
    'Groovy': '#E69F56',
    'Visual Basic': '#945DB7',
    'MATLAB': '#E16737',
    'Julia': '#A270BA',
    'Tcl': '#E4CC98',
    'Markdown': '#083FA1',
    'YAML': '#CB171E',
    'JSON': '#292929',
    'XML': '#0060AC',
    'Makefile': '#427819',
    'Dockerfile': '#384D54',
    'Terraform': '#623CE4',
    'LICENSE': '#cccccc',
}

def convert_bytes(size_bytes):
    if size_bytes == 0:
        return "0B"
    base = 1024
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    unit_index = int(math.log(size_bytes, base))
    unit_index = min(unit_index, len(units) - 1)
    converted_size = size_bytes / (base ** unit_index)
    return f"{converted_size:.0f} {units[unit_index]}"

def set_dict_value(dictionary, key, value) -> None:
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value
def get_line_count(filepath: str) -> int:
    try:
        with open(filepath,'rb') as f:
            _file = f.read()
        _file = _file.decode().splitlines()
        return len(_file)
    except Exception as e:
        print(e)
        return 0
def convert_extension_to_language(extension: str) -> str:
    for key, exts in LANGUAGE_MAPPER.items():
        if extension in exts:
            return key
    return None

def convert_hex_to_escsq(hex_color: str) -> str:
    hex_color = hex_color.lstrip('#')
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return '\033[38;2;{};{};{}m'.format(*rgb_color)

for root, dirs, files in os.walk('./'):
    for file in files:

        full_path = os.path.join(root, file)
        if full_path.startswith(tuple(FORBIDDEN_FOLDERS)): continue

        extension = file.split('.')[-1]
        lang = convert_extension_to_language(extension)
        if not lang:
            continue
        set_dict_value(LANGS, lang, os.path.getsize(full_path))
        set_dict_value(FILES, lang, 1)
        set_dict_value(LINES, lang, get_line_count(full_path))
def print_language_summary():
    total = sum(LANGS.values())
    print('Idx  | Language   |   Size    | Files| Usage' + ' ' * (BAR_LENGTH - 5) + ' | Percentage | Lines')
    for color_index,lang in enumerate(LANGS):
        
        percentage = LANGS[lang] / total
        filled_length = int(BAR_LENGTH * percentage)
        bar = '█' * filled_length + '░' * (BAR_LENGTH - filled_length)
        print(f'{str(color_index):<4} | {lang:<10} | {convert_bytes(LANGS[lang]):7}   | {FILES[lang]:4} | {convert_hex_to_escsq(LANGUAGE_COLOR[lang])}{bar}{RESET_COLOR} ({percentage:.2%}) - {LINES[lang]} lines')
    
    print(f'{sum(FILES.values())} Files')

if __name__ == "__main__":
    print_language_summary()