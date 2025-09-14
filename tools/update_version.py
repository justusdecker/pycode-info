text = ''
with open('./src/pycode_info/__init__.py') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('"').strip("'")
            version.split('.')
            major, minor, patch = map(int, version.split('.'))
            patch += 1
            version = f"{major}.{minor}.{patch}"
            text += f'__version__ = "{version}"\n'
        else:
            text += line
        
    with open('./src/pycode_info/__init__.py', 'w') as fw:
        fw.write(text)