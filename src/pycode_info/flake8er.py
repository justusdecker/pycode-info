import subprocess
import json
import os
from .utils import set_dict_value_list
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
                    for err in error_list:
                        data = {
                            "file": file,
                            "line_number": err['line_number'],
                            "column_number": err['column_number'],
                            "text": err['text']
                        }
                        set_dict_value_list(ERRORS,full_path,data)
    with open('flake8_report.json','w') as f:
        json.dump(ERRORS,f,indent=4)
