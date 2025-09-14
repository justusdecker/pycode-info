# Pycode-Info


## Code Statistics

### Language Percentage
<img width="1100" height="225" alt="fancystuff" src="https://github.com/user-attachments/assets/65f29165-e20f-4347-b14e-157c24024935" />

### Code Check

<img width="1387" height="634" alt="fancystuff3" src="https://github.com/user-attachments/assets/74817ea5-34bd-4cb1-ab74-3feae6bc4880" />

### Cyclomatic Complexity Viewer
<img width="985" height="751" alt="overly_complex" src="https://github.com/user-attachments/assets/e9917cfb-7da3-4658-9d2c-07b7d25a37cd" />

### Flake8_report.json

This will be used to show you errors & warnings

```json
{
    "./main.py": [
        {
            "file": "./main.py",
            "line_number": 5,
            "column_number": 80,
            "text": "line too long (115 > 79 characters)"
        },
        {
            "file": "./main.py",
            "line_number": 14,
            "column_number": 80,
            "text": "line too long (81 > 79 characters)"
        },
        {
            "file": "./main.py",
            "line_number": 19,
            "column_number": 5,
            "text": "'src.pycode_info.ccv.print_code_heatmap' imported but unused"
        },
        {
            "file": "./main.py",
            "line_number": 19,
            "column_number": 80,
            "text": "line too long (86 > 79 characters)"
        },
        {
            "file": "./main.py",
            "line_number": 24,
            "column_number": 80,
            "text": "line too long (105 > 79 characters)"
        }
    ]
}
```

## Upcoming

- Logical Lines: Only lines are counted that contains code
- Comment Lines: Only lines are counter that contains comments
-hotspot gatherer: gets the most edited files
- Added / Removed lines
- cyclomatic complexity viewer
