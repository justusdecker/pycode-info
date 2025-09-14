
# Coming soon

DESCRIPTION = """
Analyze code complexity and visualize as heatmap.
Language summary and file statistics included.
"""
EPILOG = "Developed by Justus Decker. - 2025. License: MIT. All rights reserved."




if __name__ == "__main__":
    import sys
    sys.argv.append('flake8')
    from src.pycode_info.ccv import print_code_heatmap, analyze_all_files_in_workspace
    from src.pycode_info.lang_info import print_language_summary
    from src.pycode_info.flake8er import print_flake8_report
    import argparse
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
    parser.add_argument('function', choices=['heatmap', 'summary', 'flake8'], help='Function to execute')

    args = parser.parse_args()
    if args.function == 'heatmap':
        analyze_all_files_in_workspace()
    elif args.function == 'summary':
        print_language_summary()
    elif args.function == 'flake8':
        print_flake8_report(line_sep=False)
