"""
This module provides ANSI escape sequences for terminal colors and a mapping of programming languages to their representative colors.

It includes a function to convert hex color codes to ANSI escape sequences for colored terminal output.

"""

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
GRAY = '\033[90m'

RESET_COLOR = '\033[0m'


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

ERROR_TO_COLOR_MAPPER = {
    'E': '#FF0000',  # Red for errors
    'W': '#FFA500',  # Orange for warnings
    'F': '#FFFF00',  # Yellow for formatting issues
    'C': '#0000FF',  # Blue for complexity issues
    'N': '#008000',  # Green for naming issues
    'D': '#800080',  # Purple for docstring issues
    'I': '#00FFFF',  # Cyan for import issues
    'T': '#FFC0CB',  # Pink for type issues
    'S': '#A52A2A',  # Brown for security issues
    'R': '#808080',  # Gray for refactor suggestions
    'Q': '#000000',  # Black for quality issues
    'X': '#FFFFFF',  # White for unknown issues
    
}



def convert_hex_to_escsq(hex_color: str) -> str:
    """
    Convert a hex color code to an ANSI escape sequence for terminal output.
    """
    hex_color = hex_color.lstrip('#')
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return '\033[38;2;{};{};{}m'.format(*rgb_color)