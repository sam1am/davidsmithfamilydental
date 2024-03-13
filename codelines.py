import os
import fnmatch

# Define the file types we're interested in
file_types = ['*.py', '*.txt', '*.md', '*.js', '*.html']

def read_gitignore():
    """Reads .gitignore and returns a list of patterns to ignore."""
    ignore_patterns = []
    try:
        with open('.gitignore', 'r') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith('#'):
                    ignore_patterns.append(stripped_line)
    except FileNotFoundError:
        print("No .gitignore file found.")
    return ignore_patterns

def should_ignore(path, ignore_patterns):
    """Checks if the given path matches any of the ignore patterns."""
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
    return False

def count_lines_of_code(directory, ignore_patterns):
    """Counts lines of code in the given directory, respecting .gitignore."""
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns)]
        for file_type in file_types:
            for filename in fnmatch.filter(files, file_type):
                if should_ignore(filename, ignore_patterns):
                    continue
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    total_lines += sum(1 for line in f)
    return total_lines

def main():
    ignore_patterns = read_gitignore()
    total_lines = count_lines_of_code('.', ignore_patterns)
    print(f'Total lines of code: {total_lines}')

if __name__ == "__main__":
    main()
