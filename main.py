# Argparse:

"""
-e=.dll;.i
-e exclude
-ff forbidden folders - not the exact path - .git will remove all filepaths that contains .git: .git / .github etc.
"""

# Coming soon

DESCRIPTION = """
Analyze code complexity and visualize as heatmap.
Language summary and file statistics included.
"""
EPILOG = "Developed by Justus Decker. - 2025. License: MIT. All rights reserved."


if __name__ == "__main__":

    from src.ccv import print_code_heatmap, analyze_all_files_in_workspace
    from src.lang_info import print_language_summary
    import argparse
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
    parser.add_argument('function', choices=['heatmap', 'summary'])

    args = parser.parse_args()
    if args.function == 'heatmap':
        analyze_all_files_in_workspace()
    elif args.function == 'summary':
        print_language_summary()
