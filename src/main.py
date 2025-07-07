from example import build_example_filesystem

# Helper functions
def handle_cd(path_str, curr_dir, curr_path):
    parts = path_str.strip().split('/')
    dir_ptr = curr_dir
    path_copy = curr_path.copy()

    for part in parts:
        if part == "" or part == ".":
            continue
        elif part == "..":
            if dir_ptr.parent:
                dir_ptr = dir_ptr.parent
                if len(path_copy) > 1:
                    path_copy.pop()
            else:
                print("Already at root.")
        else:
            found = False
            for sub in dir_ptr.subdirectories:
                if sub.name == part:
                    dir_ptr = sub
                    path_copy.append(part)
                    found = True
                    break
            if not found:
                print(f"No such directory: {part}")
                return curr_dir, curr_path  # Don't change curr_dir if any part of path fails

    return dir_ptr, path_copy

def handle_ls(curr_dir):
    if not curr_dir.subdirectories and not curr_dir.files:
        print("Empty directory")
        return

    for subdir in curr_dir.subdirectories:
        print(f"{subdir.name}")

    for file in curr_dir.files:
        print(f"{file.file_name}")


def handle_size(curr_dir):
    total = sum(file.size for file in curr_dir.files)
    for subdir in curr_dir.subdirectories:
        total += handle_size(subdir)

    return total

# Main CLI implementation
def run_cli():
    curr_dir = build_example_filesystem()
    path = ["root"]

    print("Welcome to the Directory Size Calculator App!")
    print("Type 'help' to see available commands.")

    while True:
        cmd = input(f"{'/'.join(path)}> ").strip().split()
        if not cmd:
            continue

        command = cmd[0]
        arg = cmd[1] if len(cmd) > 1 else None

        if command == "help":
            print("""
            Available commands:
            - ls             : List contents of current directory
            - cd <dir>       : Change into a subdirectory or parent directory
            - size           : Calculate total size of current directory (recursive)
            - exit           : Quit the application
            """)
        elif command == "cd":
            if not arg:
                print("Usage: cd <directory>")
                continue
            curr_dir, path = handle_cd(arg, curr_dir, path)
        elif command == "ls":
            handle_ls(curr_dir)
        elif command == "size":
            print(handle_size(curr_dir))
        elif command == "exit":
            print("Quitting the application. Goodbye!")
            break
        else:
            print("Unknown command. Type 'help' for list.")

if __name__ == '__main__':
    run_cli()