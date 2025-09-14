import subprocess
import json
import os
from .utils import set_dict_value_list
from .colors import ERROR_TO_COLOR_MAPPER,convert_hex_to_escsq, RESET_COLOR
def run_flake8(file_path):
    try:
        result = subprocess.run(
            ['flake8', file_path, '--format=json'],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        try:
            return json.loads(e.stdout)
        except json.JSONDecodeError:
            return {}

def anayze_files():
    ERRORS = {}
    for root, _, files in os.walk('./'):
        for file in files:
            if not file.endswith('.py'): continue
            full_path = os.path.join(root, file)
            errors = run_flake8(full_path)
            if errors:
                for file, error_list in errors.items():
                    lines_seen = set()
                    for err in error_list:
                        if err['line_number'] in lines_seen:
                            continue
                        data = {
                            "line_number": err['line_number'],
                            "column_number": err['column_number'],
                            "text": err['text'],
                            "code": err['code']
                        }
                        lines_seen.add(err['line_number'])
                        set_dict_value_list(ERRORS,full_path,data)
    return ERRORS

def print_flake8_report(
    truncate: int = 200, 
    max_line_length: int = 79,
    line_sep: bool = True) -> None:
    
    ERRORS = anayze_files()
    last_line = -1
    for file, error_list in ERRORS.items():
        print(f"\nFile: {file} - {len(error_list)} Errors\n", "="*50)
        with open(file, 'r') as f:
            file_content = f.readlines()

        for err in error_list:
            line, column, text, code = err.values()
            
            if line != last_line and line_sep: #! Make this optinional
                last_line = line
                print("-"*50)

            if line > truncate:
                print("... (truncated)")
                break

            code[0].upper()
            color = ERROR_TO_COLOR_MAPPER.get(code[0].upper(), '#FFFFFF')
            truncated_line = file_content[line-1].replace('\n', '')
            if len(truncated_line) > max_line_length:
                truncated_line = truncated_line[:max_line_length:] + '...'
            
            filled_line = truncated_line.ljust(max_line_length + 3) # <- 3 is the length of the dots
            print(f"{convert_hex_to_escsq(color)}{line:4d} |{filled_line}{RESET_COLOR} <-- {code} {text}")