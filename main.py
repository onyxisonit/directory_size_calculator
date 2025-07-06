from file_system import File, Directory
from example import build_example_filesystem

# Helper functions
def handle_cd(arg, curr_dir):
    if arg == "..":
        if curr_dir.parent:
           return curr_dir.parent
        else:
            print("Already at root directory")
            return curr_dir

    for subdir in curr_dir.subdirectories:
        if subdir.name == arg:
            return subdir

    print(f"No such directory: {arg}")
    return curr_dir

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

def main():
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
            if arg:
                new_dir = handle_cd(arg, curr_dir)
                if new_dir != curr_dir:
                    if arg == "..":
                        path.pop()
                    else:
                        path.append(arg)
                    curr_dir = new_dir
                else:
                    print("Usage: cd <directory>")
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
    main()