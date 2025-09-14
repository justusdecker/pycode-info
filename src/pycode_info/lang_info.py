import os
import math
from .colors import RESET_COLOR, LANGUAGE_COLOR, convert_hex_to_escsq
from .utils import set_dict_value

FORBIDDEN_FOLDERS = ['.git','.vscode','.pytest','build','dist']

BAR_LENGTH = 50

LANGS, FILES, LINES = {}, {},{}

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

def convert_bytes(size_bytes):
    """
    Convert bytes to a human-readable format (e.g., KB, MB, GB).
    Returns a string representation of the size.
    """
    if size_bytes == 0:
        return "0B"
    base = 1024
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    unit_index = int(math.log(size_bytes, base))
    unit_index = min(unit_index, len(units) - 1)
    converted_size = size_bytes / (base ** unit_index)
    return f"{converted_size:.0f} {units[unit_index]}"


        
def get_line_count(filepath: str) -> int:
    """
    Get the number of lines in a file.
    Returns 0 if the file cannot be read.
    """
    try:
        with open(filepath,'rb') as f:
            _file = f.read()
        _file = _file.decode().splitlines()
        return len(_file)
    except Exception as e:
        print(e)
        return 0
    
def convert_extension_to_language(extension: str) -> str:
    """
    Convert a file extension to its corresponding programming language.
    Returns None if the extension is not recognized.
    """
    for key, exts in LANGUAGE_MAPPER.items():
        if extension in exts:
            return key
    return None

def analyze_all_files_in_workspace() -> None:
    """
    Get language usage statistics for all files in the current workspace.
    Populates the LANGS, FILES, and LINES dictionaries with size, file count, and line count per language.
    Clears previous data before analysis.
    Returns nothing.
    """
    
    LANGS.clear()
    LINES.clear()
    FILES.clear()
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
    """
    Visualize language usage statistics as a summary table.
    Displays size, file count, usage bar, percentage, and line count per language.
    """
    analyze_all_files_in_workspace()
    total = sum(LANGS.values())
    print('Idx  | Language   |   Size    | Files| Usage' + ' ' * (BAR_LENGTH - 5) + ' | Percentage | Lines')
    for color_index,lang in enumerate(LANGS):
        
        percentage = LANGS[lang] / total
        filled_length = int(BAR_LENGTH * percentage)
        bar = '█' * filled_length + '░' * (BAR_LENGTH - filled_length)
        print(f'{str(color_index):<4} | {lang:<10} | {convert_bytes(LANGS[lang]):7}   | {FILES[lang]:4} | {convert_hex_to_escsq(LANGUAGE_COLOR[lang])}{bar}{RESET_COLOR} ({percentage:.2%}) - {LINES[lang]} lines')
    
    print(f'{sum(FILES.values())} Files')
