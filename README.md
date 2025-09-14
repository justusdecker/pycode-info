# Pycode-Info

**Pycode-Info** is a Python toolkit for analyzing codebases. It provides language statistics, code complexity heatmaps, and integrates with Flake8 for linting reports. The tool is designed to help developers quickly understand the structure and quality of their code.

---

## Features

- **Language Statistics:**  
  Summarizes the programming languages in your project, showing file counts, total size, and line counts per language with a visual usage bar.

- **Cyclomatic Complexity Viewer:**  
  Analyzes Python files for cyclomatic complexity, highlighting complex functions and providing a heatmap of code complexity.

- **Flake8 Integration:**  
  Runs Flake8 on all Python files and summarizes errors and warnings in a readable format.

---

## Example Outputs

### Language Percentage

![Language Percentage](https://github.com/user-attachments/assets/cce5a4da-c5ba-48ae-9628-b6af34bdfc5f)

### Code Check

![Code Check](https://github.com/user-attachments/assets/74817ea5-34bd-4cb1-ab74-3feae6bc4880)

### Cyclomatic Complexity Viewer

![Cyclomatic Complexity Viewer](https://github.com/user-attachments/assets/e9917cfb-7da3-4658-9d2c-07b7d25a37cd)

---

## Flake8 Report Example

The Flake8 report summarizes errors and warnings in your codebase:

```json
{
    "./main.py": [
        {
            "line_number": 5,
            "column_number": 80,
            "text": "line too long (115 > 79 characters)",
            "code": "E501"
        },
        {
            "line_number": 14,
            "column_number": 80,
            "text": "line too long (81 > 79 characters)",
            "code": "E501"
        }
    ]
}
```

---

## Usage

### Command Line

Run the tool from your project root:

```sh
python main.py summary      # Show language statistics
python main.py heatmap      # Show cyclomatic complexity heatmap for all Python files
python main.py flake8       # Run Flake8 and print a summary report
```

### As a Module

You can also use the main features in your own scripts:

```py
from pycode_info.lang_info import print_language_summary
from pycode_info.ccv import analyze_all_files_in_workspace
from pycode_info.flake8er import print_flake8_report

print_language_summary()
analyze_all_files_in_workspace()
print_flake8_report()
```

---

## Upcoming Features

- **Logical Lines:** Count only lines containing code.
- **Comment Lines:** Count only lines containing comments.
- **Hotspot Gatherer:** Identify the most edited files.
- **Added/Removed Lines:** Track code churn.
- **Cyclomatic Complexity Viewer:** Enhanced visualization and reporting.

---

## License

MIT License  
Developed by Justus Decker - Copyright 2025
