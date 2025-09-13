import ast
import os
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET_COLOR = '\033[0m'

class ComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 1

    def visit_If(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)
        
    def visit_While(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.complexity += len(node.values) - 1
        self.generic_visit(node)

class HotSpotVisitor(ast.NodeVisitor):
    def __init__(self):
        self.complexities = {}
        self.current_function = None
        
    def visit_FunctionDef(self, node):
        self.current_function = node.name
        self.complexities[node.name] = {
            'complexity': 1,
            'start_line': node.lineno,
            'end_line': node.end_lineno
        }
        self.generic_visit(node)
        self.current_function = None

    def visit_If(self, node):
        if self.current_function:
            self.complexities[self.current_function]['complexity'] += 1
        self.generic_visit(node)

    def visit_For(self, node):
        if self.current_function:
            self.complexities[self.current_function]['complexity'] += 1
        self.generic_visit(node)
    
    def visit_While(self, node):
        if self.current_function:
            self.complexities[self.current_function]['complexity'] += 1
        self.generic_visit(node)
        
    def visit_ExceptHandler(self, node):
        if self.current_function:
            self.complexities[self.current_function]['complexity'] += 1
        self.generic_visit(node)
        
    def visit_BoolOp(self, node):
        if self.current_function:
            self.complexities[self.current_function]['complexity'] += 1
        self.generic_visit(node)

def calculate_cyclomatic_complexity(code_string) -> int:
    """
    Calculate the cyclomatic complexity of a given Python code string.
    Returns the complexity as an integer.
    Returns -1 if the code cannot be parsed.
    """
    try:
        tree = ast.parse(code_string)
        visitor = ComplexityVisitor()
        visitor.visit(tree)
        return visitor.complexity
    except SyntaxError:
        return -1

def get_hotspots_by_complexity(code_string, max_complexity):
    """
    Get functions in the code string that exceed the specified cyclomatic complexity.
    Returns a dictionary of function names with their complexity and line numbers.
    Returns {"error": "Invalid Python code"} if the code cannot be parsed.
    """
    try:
        tree = ast.parse(code_string)
        visitor = HotSpotVisitor()
        visitor.visit(tree)
        
        hotspots = {}
        for func_name, data in visitor.complexities.items():
            if data['complexity'] > max_complexity:  # Schwellenwert für Hotspot
                hotspots[func_name] = data
        return hotspots
    except SyntaxError:
        return {"error": "Invalid Python code"}

def get_complexity_for(filepath: str) -> str | int:
    """
    Reads a Python file
    Get the cyclomatic complexity for a given Python file.
    Returns the complexity as an integer.
    """
    with open(filepath) as f:
        return calculate_cyclomatic_complexity(f.read())

def print_hotspots_for(filepath: str) -> dict:
    """
    Display functions in the given Python file that exceed a certain cyclomatic complexity.
    Prints the function name, complexity, and line numbers.
    Returns a dictionary of hotspots.
    """
    hotspots = get_hotspots_for(filepath)
    if hotspots:
        for func, data in hotspots.items():
            print(f"Hotspot found")
            print(f'├ Name: {func}')
            print(f"├ Complexity: {data['complexity']}")
            print(f"└ Lines: {data['start_line']} - {data['end_line']}")

def get_hotspots_for(filepath: str, max_complexity) -> dict:
    with open(filepath) as f:
        return get_hotspots_by_complexity(f.read(), max_complexity)

def print_code_heatmap(filepath, pok: bool = False, max_complexity: int = 10):
    """
    Display a heatmap of code complexity for a given Python file.
    Lines with complexity above the max_complexity threshold are highlighted.
    """
    complexities = get_hotspots_for(filepath, max_complexity)
    if "error" in complexities:
        print(f"ParseError: {complexities['error']}")
        return False
    print('-'*15,filepath.replace('\\','/').split('/')[-1],'-'*15)
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    has_problem = False
    for line_num, line_content in enumerate(lines, 1):
        color = RESET_COLOR
        for func_name, data in complexities.items():
            if data['start_line'] <= line_num <= data['end_line']:
                # Farbauswahl basierend auf Komplexität im Verhältnis zum Maximum
                if not has_problem:
                    has_problem = data['complexity'] > max_complexity
                if data['complexity'] > max_complexity * 1.5:
                    print(f"{RED}{line_num:4d} |{line_content.rstrip()}{RESET_COLOR}")
                elif data['complexity'] > max_complexity:
                    print(f"{YELLOW}{line_num:4d} |{line_content.rstrip()}{RESET_COLOR}")
                else:
                    if pok:
                        print(f"{GREEN}{line_num:4d} |{line_content.rstrip()}{RESET_COLOR}")
                break
    return has_problem

def analyze_all_files_in_workspace():
    """
    Analyze all Python files in the current workspace and print a complexity heatmap for each.
    Prompts the user to press <ENTER> to continue after each file with complexity issues.
    """
    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                if print_code_heatmap(full_path):
                    input('Press <ENTER> to continue')