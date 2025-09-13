import subprocess
import json

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

import os
for root, dirs, files in os.walk('./'):
    for file in files:
        if not file.endswith('.py'):
            continue
        full_path = os.path.join(root, file)
        errors = run_flake8(full_path)

        if errors:
            print(f"Flake8-Error in {full_path}:")
            for file, error_list in errors.items():
                for err in error_list:
                    print(f"- {err['line_number']}, {err['column_number']}: {err['code']} {err['text']}")
        else:
            print(f"No Flake8-Errors found in {full_path}.")